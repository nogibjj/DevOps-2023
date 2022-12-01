#!/usr/bin/env python
"""Geocli: a command-line interface for geospatial tools.
Uses the click library to build a command-line interface for the geotools
"""

import click
from mylib.geotools import get_distance, get_populous_cities


@click.group()
def cli():
    """Geocli: a command-line interface for geospatial tools."""


@cli.command("distance")
@click.argument("city1", type=str, default="New York, NY")
@click.argument("city2", type=str, default="Los Angeles, CA")
def distance_cli(city1, city2):
    """Get the distance between two cities.
    Example:
    $ ./geocli distance "New York, NY" "Los Angeles, CA"

    """

    # get the distance between two cities
    distance = get_distance(city1, city2)
    # print the distance using different colors for cities and distance
    click.secho(city1, fg="green", nl=False)
    click.secho(" to ", nl=False)
    click.secho(city2, fg="green", nl=False)
    click.secho(" is ", nl=False)
    click.secho(f"{distance:.2f} miles", fg="blue")


@cli.command("cities")
def cities_cli():
    """Get a list of the 10 most populous cities in the USA."""
    # get a list of the 10 most populous cities in the usa
    cities = get_populous_cities()
    # print the cities
    for city in cities:
        click.secho(city, fg="green")


if __name__ == "__main__":
    cli()
