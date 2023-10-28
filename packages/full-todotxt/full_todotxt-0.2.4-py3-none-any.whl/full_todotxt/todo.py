import re

from datetime import datetime, date
from typing import Union, List, Callable, Optional
from pathlib import Path

import click
from pytodotxt.todotxt import Task  # type: ignore[import]

PathIsh = Union[Path, str]


def _prompt_todo_text(full_screen: bool) -> Optional[str]:
    # prompt the user for a new todo (just the text)
    todo_text: Optional[str] = None
    if full_screen:
        from prompt_toolkit.shortcuts import input_dialog

        todo_text = input_dialog(title="Add Todo:").run()
    else:
        todo_text = click.prompt("[Todo]> ", prompt_suffix="")

    if not todo_text:
        return None
    elif not todo_text.strip():
        if full_screen:
            from prompt_toolkit.shortcuts import message_dialog

            message_dialog(title="Error", text="No input provided for the todo").run()
        else:
            click.echo("No input provided for the todo", err=True)
        return None

    return todo_text


Projects = Union[List[str], Callable[[], List[str]]]


def _prompt_projects(
    todo_text: str,
    projects: Projects,
    full_screen: bool,
) -> str:
    from prompt_toolkit.formatted_text import HTML

    projects_raw: str = ""
    # if you provided a project in the text itself, skip forcing you to specify one
    if len(Task(todo_text).projects) == 0:
        from prompt_toolkit.completion import FuzzyWordCompleter

        projects_lst = projects() if callable(projects) else projects

        from prompt_toolkit.document import Document
        from prompt_toolkit.validation import Validator, ValidationError

        class ProjectTagValidator(Validator):
            def validate(self, document: Document) -> None:
                text = document.text

                if len(text.strip()) == 0:
                    raise ValidationError(
                        message="You must specify at least one project tag"
                    )

                # check if all input matches '+projectag'
                for project_tag in text.split():
                    if not bool(re.match(r"\+\w+", project_tag)):
                        raise ValidationError(
                            message=f"'{project_tag}' doesn't look like a project tag. e.g. '+home'"
                        )

        # project tags
        click.echo("Enter one or more tags, hit 'Tab' to autocomplete")
        from prompt_toolkit.shortcuts.prompt import prompt

        projects_raw = prompt(
            "[Enter Project Tags]> ",
            completer=FuzzyWordCompleter(projects_lst),
            complete_while_typing=True,
            validator=ProjectTagValidator(),
            bottom_toolbar=HTML("<b>Todo:</b> {}".format(todo_text)),
        )

    return projects_raw


def _prompt_priority(full_screen: bool) -> str:
    # select priority
    if full_screen:
        from prompt_toolkit.shortcuts import button_dialog

        todo_priority: str = button_dialog(
            title="Priority:",
            text="A is highest, C is lowest",
            buttons=[
                ("A", "A"),
                ("B", "B"),
                ("C", "C"),
            ],
        ).run()
    else:

        def prompt_priority() -> Optional[str]:
            click.echo("Enter a priority: (A, B, or C): ", nl=False)
            prio: str = click.getchar().upper().strip()
            click.echo()
            if prio not in ["A", "B", "C"]:
                click.echo(f"Invalid priority '{prio}'")
                return None
            return prio

        resp: Optional[str] = None
        while resp not in ["A", "B", "C"]:
            resp = prompt_priority()
        assert resp in ["A", "B", "C"]
        todo_priority = resp

    return todo_priority


def _prompt_deadline(full_screen: bool, date_format: str) -> Optional[datetime]:
    # ask if the user wants to add a time
    if full_screen:
        from prompt_toolkit.shortcuts import button_dialog

        add_time: bool = button_dialog(
            title="Deadline:",
            text="Do you want to add a deadline for this todo?",
            buttons=[
                ("No", False),
                ("Yes", True),
            ],
        ).run()
    else:
        add_time = click.confirm(
            "Do you want to add a deadline for this todo?", default=True
        )

    # prompt for adding a deadline
    todo_time: Optional[datetime] = None
    if add_time:
        while todo_time is None:
            if full_screen:
                from prompt_toolkit.shortcuts import input_dialog, message_dialog

                todo_time_str: Optional[str] = input_dialog(
                    title="Describe the deadline.",
                    text="For example:\n'9AM', 'noon', 'tomorrow at 10PM', 'may 30th at 8PM'",
                ).run()
                # if user hit cancel
                if todo_time_str is None:
                    add_time = False
                    break
                else:
                    import dateparser

                    todo_time = dateparser.parse(
                        todo_time_str, settings={"PREFER_DATES_FROM": "future"}
                    )
                    if todo_time is None:
                        message_dialog(
                            title="Error",
                            text="Could not parse '{}' into datetime".format(
                                todo_time_str
                            ),
                        ).run()
            else:
                from autotui.options import Option, options
                from autotui.prompts import prompt_datetime

                with options(Option.LIVE_DATETIME):
                    todo_time = prompt_datetime(prompt_msg="[Deadline]> ")

    if todo_time is not None:
        # floor the time to the nearest minute
        todo_time = todo_time.replace(second=0, microsecond=0)

        # if the user didn't specify a timezone, assume they meant their local timezone
        if todo_time.tzinfo is None:
            todo_time = todo_time.replace(tzinfo=datetime.now().astimezone().tzinfo)

        return todo_time
    else:
        return None


# prompt the user to add a todo
def prompt_todo(
    *,
    add_due: bool,
    date_format: str,
    projects: Union[List[str], Callable[[], List[str]]],
    add_deadline: bool,
    full_screen: bool = True,
) -> Optional[Task]:
    todo_text: Optional[str] = _prompt_todo_text(full_screen)
    if todo_text is None:
        return None

    projects_raw: str = _prompt_projects(todo_text, projects, full_screen)
    todo_priority: str = _prompt_priority(full_screen)
    if add_deadline:
        todo_time: Optional[datetime] = _prompt_deadline(full_screen, date_format)
    else:
        todo_time = None

    # construct the Task
    constructed: str = f"({todo_priority})"
    constructed += f" {date.today()}"
    constructed += f" {todo_text}"
    if projects_raw.strip():
        constructed += f" {projects_raw}"
    if todo_time is not None:
        constructed += f" deadline:{datetime.strftime(todo_time, date_format)}"
        if add_due:
            constructed += f" due:{datetime.strftime(todo_time, r'%Y-%m-%d')}"

    return Task(constructed)
