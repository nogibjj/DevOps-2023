"""Build a library of geospatial tools."""

from geopy import distance, geocoders

USER_AGENT = "python-for-devops-tutorial"

# create a function return a list of the 10 most populous cities in the usa
def get_populous_cities():
    """Return a list of the 10 most populous cities in the USA."""
    # create a list of the 10 most populous cities in the usa
    cities = [
        "New York, NY",
        "Los Angeles, CA",
        "Chicago, IL",
        "Houston, TX",
        "Philadelphia, PA",
        "Phoenix, AZ",
        "San Antonio, TX",
        "San Diego, CA",
        "Dallas, TX",
        "San Jose, CA",
    ]
    # return the list of cities
    return cities


# create a function to return the distance between two cities
def get_distance(city1, city2):
    """Return the distance between two cities."""
    # create a geolocator
    geolocator = geocoders.Nominatim(user_agent=USER_AGENT)
    # get the location of city1
    location1 = geolocator.geocode(city1)
    # get the location of city2
    location2 = geolocator.geocode(city2)
    # return the distance between the two cities
    return distance.distance(location1.point, location2.point).miles
