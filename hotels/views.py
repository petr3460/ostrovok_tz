from django.shortcuts import render
from .models import City, Hotel
from django.http import JsonResponse



def home(request):
    if request.method == 'GET':
        cities = City.objects.all()
        context = {'cities': cities}
        return render(request, 'home.html', context)

    if request.method == 'POST':
        count = request.POST.get('count') or 0
        show_button_again = 1
        print('=====COUNT IS : ======= ', count)

        if count:
            count = int(count)
            hotels = Hotel.objects.filter(city=request.POST.get('cityselect'))[count:count+3]

        else:
            hotels = Hotel.objects.filter(city=request.POST.get('cityselect'))[:3]

        if not Hotel.objects.filter(city=request.POST.get('cityselect'))[count + 3:]:
            show_button_again = 0

        return JsonResponse({'hotels': list(hotels.values()), 'show_button': show_button_again})