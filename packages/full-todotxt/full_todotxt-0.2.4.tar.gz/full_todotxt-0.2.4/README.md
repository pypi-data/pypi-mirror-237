# full-todotxt

[![PyPi version](https://img.shields.io/pypi/v/full_todotxt.svg)](https://pypi.python.org/pypi/full_todotxt) [![Python 3.8|3.9|3.10|3.11](https://img.shields.io/pypi/pyversions/full_todotxt.svg)](https://pypi.python.org/pypi/full_todotxt)

[todotxt](https://github.com/todotxt/todo.txt) interactive interface that forces you to specify certain attributes.

<img src="https://raw.githubusercontent.com/seanbreckenridge/full_todotxt/master/.github/demo.gif" alt="demo gif">

For each todo, you have to specify at least `one project tag` (e.g. `+work`) and a priority `(A)`.

Though not required for each todo, it will prompt you want to specify a `deadline`, which will store a `deadline` key-value pair to the todo with the datetime as the value.

For example:

```
(A) measure space for shelving +home deadline:2020-05-13-15-30
```

... which specifies 2020-05-13 at 3:30PM.

If the `todo.txt` file is not provided as the first argument, it tries to guess based on typical locations

The `my.todotxt.active` module in [HPI](https://github.com/seanbreckenridge/HPI) parses the deadline back into python:

```
$ hpi query my.todotxt.active.todos -s | jq 'select(.deadline) | .raw' -r
(C) 2023-10-01 drink water +self deadline:2023-10-02T00-00-0700
```

## Installation

#### Requires:

`python3.8+`

To install with pip, run:

    python3 -m pip install full-todotxt

## Usage

```
Usage: full_todotxt [OPTIONS] [TODOTXT_FILE]

  If TODOTXT_FILE is not specified, the environment variable FULL_TODOTXT_FILE will be used.

Options:
  --add-due / --no-add-due        Add due: key/value flag based on deadline:  [default: no-add-due]
  -t, --time-format TEXT          Specify a different time format for deadline:  [env var: FULL_TODOTXT_TIME_FORMAT;
                                  default: %Y-%m-%d-%H-%M]
  -f, --full-screen / -p, --prompts
                                  Use prompts or the full screen dialog editor [default: full-screen]
  -h, --help                      Show this message and exit.
```

This checks many possible locations for the `todo.txt` file:

- `TODOTXT_FILE` passed to `full_todotxt`
- `$FULL_TODOTXT_FILE` environment variable
- `$TODO_DIR/todo.txt`
- `$XDG_CONFIG_HOME/todo/todo.txt`
- `~/.config/todo/todo.txt`
- `~/.todo/todo.txt`
- `~/.todo.txt`
- `~/todo.txt`
