import csv
from hotels.models import *
def run():


    with open('hotels.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                int_id = int(row[5])
            except:
                continue

            if not City.objects.filter(id=int_id):
                city = City(id=int_id, name=row[1])
                city.save()
            else:
                city = City.objects.get(id=int_id)

            hotel = Hotel(name=row[2], slug=row[0], city=city, price=float(row[9]), image=row[3])
            hotel.save()



