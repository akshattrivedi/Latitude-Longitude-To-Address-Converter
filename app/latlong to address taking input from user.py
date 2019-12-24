from geopy.geocoders import Nominatim #for getting location from latitute and longitude

#initialisation
geolocator = Nominatim(user_agent="App",timeout=100)

#taking input
lat = input("Enter Latitude")
lon = input("Enter Lon")

s = str(lat) + "," + str(lon)

location = geolocator.reverse(s)
#getting address of location
strt = location.address
print(strt)


