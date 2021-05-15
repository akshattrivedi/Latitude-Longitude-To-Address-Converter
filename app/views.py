from django.shortcuts import render,redirect
from app.latLongToAddressConverter import findAddress

# Create your views here.
def index(request):
    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']

        streetAddress = findAddress(lat, lon)
        context = {'streetAddress':streetAddress}
        return render(request,'app/index.html',context)

    else:
        return render(request,'app/index.html')
