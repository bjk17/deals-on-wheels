from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True)

    def get_list_of_manufacturers(self):
        return [str(m) for m in self.Manufacturer.all()]

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=10)
    driven = models.IntegerField()
    year = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True)
    registered_at = models.DateField(null=True, blank=True)
    next_check = models.DateField(null=True, blank=True)
    pollution = models.CharField(max_length=100, null=True, blank=True)


    def get_list_of_cars(self):
        return [str(c) for c in self.Car.all()]

    def __str__(self):
        return "{} {}, {}".format(self.manufacturer, self.model, self.year)


class Advertisement(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)
    price = models.IntegerField()

    currency_choices = (
        ('ISK', 'Icelandic kronors'),
        ('USD', 'US Dollars'),
        ('EUR', 'Euros'),
        ('BTC', 'Bitcoin')
    )
    currency = models.CharField(
        max_length=3,
        choices=currency_choices,
        default='ISK',
    )

    description = models.CharField(max_length=1000, blank=True)

    def get_list_of_advertisements(self):
        return [str(a) for a in self.Advertisement.all()]

    def __str__(self):
        return "User '{}' selling '{}' for {}".format(self.seller.username, self.car, self.price)
