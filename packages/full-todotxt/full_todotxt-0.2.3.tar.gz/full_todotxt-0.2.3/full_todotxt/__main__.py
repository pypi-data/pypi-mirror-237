import os
from typing import Optional, List, Set
from pathlib import Path

import click

from shutil import copyfile
from pytodotxt.todotxt import TodoTxt, Task  # type: ignore[import]

from .todo import prompt_todo, PathIsh


def full_backup(todotxt_file: PathIsh) -> None:
    """
    Backs up the todo.txt file before writing to it
    """

    backup_file: PathIsh = f"{todotxt_file}.full.bak"
    copyfile(str(todotxt_file), str(backup_file))


def parse_projects(todo_sources: List[TodoTxt]) -> Set[str]:
    """Get a list of all tags from the todos"""
    projects = set()
    for tf in todo_sources:
        for todo in tf.tasks:
            for proj in todo.projects:
                projects.add(f"+{proj}")
    return projects


def parse_all_projects(todo_file: TodoTxt) -> List[str]:
    # list of sources, done.txt will be added if it exists
    todo_sources: List[TodoTxt] = [todo_file]

    done_file: Path = todo_file.filename.parent / "done.txt"
    if done_file.exists():
        todo_sources.append(TodoTxt(done_file))

    for t in todo_sources:
        t.parse()

    return list(parse_projects(todo_sources))


def locate_todotxt_file(todotxt_filepath: Optional[Path]) -> Path:
    if todotxt_filepath is not None:
        if not os.path.exists(todotxt_filepath):
            raise click.BadParameter(
                f"The provided file '{todotxt_filepath}' does not exist."
            )
        else:
            return todotxt_filepath
    else:  # no todo file passed, test some common locations
        home = Path.home()
        possible_locations = [
            home / ".config/todo/todo.txt",
            home / ".todo/todo.txt",
            home / ".todo.txt",
            home / "todo.txt",
        ]
        if "XDG_CONFIG_HOME" in os.environ:
            possible_locations.insert(
                0, Path(os.environ["XDG_CONFIG_HOME"]) / "todo/todo.txt"
            )
        if "TODO_DIR" in os.environ:
            possible_locations.insert(0, Path(os.environ["TODO_DIR"]) / "todo.txt")
        for p in possible_locations:
            if p.exists():
                click.echo(f"Found todo.txt file at '{p}'...", err=True)
                return p
        else:
            raise click.BadParameter(
                f"Could not find a todo.txt file in any of the following locations:\n{os.linesep.join(str(p) for p in possible_locations)}"
            )


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"], max_content_width=120)
)
@click.argument(
    "TODOTXT_FILE",
    type=click.Path(exists=True, path_type=Path),
    envvar="FULL_TODOTXT_FILE",
    default=None,
    required=False,
    callback=lambda _ctx, _param, value: locate_todotxt_file(value),
)
@click.option(
    "--add-due/--no-add-due",
    is_flag=True,
    default=False,
    help="Add due: key/value flag based on deadline:",
    show_default=True,
)
@click.option(
    "-t",
    "--time-format",
    default="%Y-%m-%dT%H-%M%z",
    envvar="FULL_TODOTXT_TIME_FORMAT",
    show_envvar=True,
    show_default=True,
    help="Specify a different time format for deadline:",
)
@click.option(
    "-f/-p",
    "--full-screen/--prompts",
    "full_screen",
    is_flag=True,
    default=True,
    help="Use prompts or the full screen dialog editor [default: full-screen]",
)
@click.option(
    "-s",
    "--skip-deadline",
    is_flag=True,
    default=False,
    help="Skip the deadline prompt",
    show_default=True,
)
def cli(
    todotxt_file: Path,
    full_screen: bool,
    add_due: bool,
    time_format: str,
    skip_deadline: bool,
) -> None:
    """
    If TODOTXT_FILE is not specified, the environment variable FULL_TODOTXT_FILE will be used.
    """
    # read from main todo.txt file
    todos: TodoTxt = TodoTxt(todotxt_file)
    todos.parse()

    # sanity check to make sure we parsed tasks correctly
    todo_lines = [
        t for t in Path(todotxt_file).read_text().strip().splitlines() if t.strip()
    ]
    assert len(todo_lines) == len(todos.tasks), "Line count and task count do not match"

    # backup todo.txt file
    full_backup(todotxt_file)

    # prompt user for new todo
    new_todo: Optional[Task] = prompt_todo(
        add_due=add_due,
        date_format=time_format,
        projects=lambda: parse_all_projects(todos),
        full_screen=full_screen,
        add_deadline=not skip_deadline,
    )

    # write back to file
    if new_todo is not None:
        todos.tasks.append(new_todo)
        click.echo(
            "{}: {}".format(click.style("Adding Todo", fg="green"), str(new_todo))
        )
        todos.save(safe=True)


if __name__ == "__main__":
    cli(prog_name="full_todotxt")
