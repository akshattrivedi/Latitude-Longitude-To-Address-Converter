from geopy.geocoders import Nominatim #for getting location from latitute and longitude

# initialisation

def findAddress(lat, lon):
    geolocator = Nominatim(user_agent="App",timeout=100)

    if not (isFloat(lat) and isFloat(lon)):
        return "Incorrect Co-ordinates Input"

    s = str(lat) + "," + str(lon)

    # Getting Street Address of the Location
    location = geolocator.reverse(s)

    if location == None:
        return "Location's Street Address Not Found!"
    else:
        strt = location.address
        return strt

def isFloat(value: str):
    try:
        float(value)
        return True
    except ValueError:
        return False

