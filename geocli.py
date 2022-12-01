#!/usr/bin/env python
"""Geocli: a command-line interface for geospatial tools.
Uses the click library to build a command-line interface for the geotools
"""

import click
from mylib.geotools import get_distance, get_populous_cities
from mylib.wiki import get_wiki_keywords

# create a function that dedupes phrases
def dedupe_phrases(phrases):
    """Remove duplicate phrases from a list of phrases."""
    # create a set of phrases
    phrase_set = set()
    # loop through the phrases
    for phrase in phrases:
        # add the phrase to the set
        phrase_set.add(phrase[0])
    # return the set of phrases
    return phrase_set


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


# create a command to get the keywords of a city
# by default only return the top 5 keywords
@cli.command("keywords")
@click.argument("city", type=str, default="New York, NY")
@click.option("--top", type=int, default=5)
def keywords_cli(city, top):
    """Get the keywords of a city.
    Example:
    $ ./geocli keywords "New York, NY" --top 5

    """

    # get the keywords of a city
    keywords = get_wiki_keywords(city)
    # dedupe the phrases
    phrases = dedupe_phrases(keywords)
    # print the top phrases
    for phrase in list(phrases)[:top]:
        click.secho(phrase, fg="green")


if __name__ == "__main__":
    cli()
