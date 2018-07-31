from django.db import models


class City(models.Model):
    name = models.CharField(max_length=40)
    #slug = models.SlugField()

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=40)
    #slug = models.SlugField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
