from django.db import models


class City(models.Model):
    name = models.CharField(max_length=40)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=50, db_index=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name
