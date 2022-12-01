#!/usr/bin/env python

"""
Main cli or app entry point
"""

from mylib.calculator import add
import click


@click.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    """Add two numbers

    Args:
        a (int): first number
        b (int): second number
    Example:
        $ ./main.py add 1 2

    """
    click.echo(add(a, b))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    add_cli()
