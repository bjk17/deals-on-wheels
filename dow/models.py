from django.db import models
from django.contrib.auth.models import User


# Overwriting 'User' class 'natural_key' function to better fit our format
def user_natural_key(self):
    return {'username': self.get_username()}


User.natural_key = user_natural_key


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True)

    def get_list_of_manufacturers(self):
        return [str(m) for m in self.Manufacturer.all()]

    def natural_key(self):
        return {'name': self.name, 'description': self.description}

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=10)
    year = models.IntegerField()
    driven = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    registered_at = models.CharField(max_length=8, null=True, blank=True)
    next_check = models.CharField(max_length=8, null=True, blank=True)
    pollution = models.CharField(max_length=100, null=True, blank=True)

    def get_list_of_cars(self):
        return [str(c) for c in self.Car.all()]

    def natural_key(self):
        return {
            'manufacturer': self.manufacturer.name,
            'model': self.model,
            'registration_number': self.registration_number,
            'color': self.color,
            'year': self.year,
            'driven': self.driven,
            'weight': self.weight,
            'registered_at': self.registered_at,
            'next_check': self.next_check,
            'pollution': self.pollution
        }

    def __str__(self):
        return "({}) {} {}, {}".format(self.registration_number, self.manufacturer, self.model, self.year)


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
