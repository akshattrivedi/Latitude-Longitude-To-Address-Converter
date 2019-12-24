from django.shortcuts import render,redirect
from geopy.geocoders import Nominatim

# Create your views here.
def index(request):
    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']
        geolocator = Nominatim(user_agent="App",timeout=100)

        
        print(lat,lon)
        s = str(lat) + "," + str(lon)

        location = geolocator.reverse(s)
        strt = location.address
        print(strt)
        context = {'street':strt}
        return render(request,'app/index.html',context)

    else:
        return render(request,'app/index.html')
