from fastapi import FastAPI
import uvicorn
from mylib.geotools import get_distance, get_populous_cities
from mylib.wiki import get_wiki_keywords


app = FastAPI()


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello FastAPI"}


# build a route to return the top 10 cities
@app.get("/cities")
async def cities_route():
    """Return the top 10 cities in the USA"""
    # get the list of cities
    cities = get_populous_cities()
    # return the list of cities
    return {"cities": cities}


# build a route to return the distance between two cities
@app.post("/distance")
async def distance_route(city1: str, city2: str):
    """Return the distance between two cities"""
    # get the distance between the two cities
    distance = get_distance(city1, city2)
    # return the distance between the two cities
    return {"distance": distance}


# build a route to return the keywords from a wikipedia page
@app.post("/keywords")
async def keywords_route(url: str):
    """Return the keywords from a wikipedia page"""
    # get the keywords from the wikipedia page
    keywords = get_wiki_keywords(url)
    # return the keywords from the wikipedia page
    return {"keywords": keywords}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
