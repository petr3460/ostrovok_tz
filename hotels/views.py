from django.shortcuts import render
from .models import City, Hotel
from django.http import HttpResponse, JsonResponse
import json
import pdb
# Create your views here.


def home(request):
    if request.method == 'GET':
        cities = City.objects.all()
        context = {'cities': cities}
        return render(request, 'home.html', context)

    if request.method == 'POST':

        hotels = Hotel.objects.filter(city=request.POST.get('cityselect')).values()
        print(hotels)
        #pdb.set_trace()
        return JsonResponse({'hotels': list(hotels)})