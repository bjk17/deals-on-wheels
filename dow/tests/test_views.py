from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from dow.views import create_advertisement
from django.contrib.auth.models import User
from dow.models import Manufacturer, Car, Advertisement
import json


class ViewsTests(TestCase):
    new_ad_json = {
        'username': "Bob",
        'manufacturer': "Porche",
        'model': "911 Carrera",
        'registration_number': "Cool kid",
        'color': "blue",
        'year': 2008,
        'weight': None,
        'registered_at': None,
        'next_check': None,
        'pollution': None,
        'image_url': "https://s1.cdn.autoevolution.com/images/gallery/PORSCHE-911-Carrera-S--997--3811_24.jpg",
        'price': 7990000,
        'description': "A very fast car for very cool people. A very fast car for very cool people. A very fast car for very cool people."
    }

    def test_GET_instead_of_POST(self):
        request = HttpRequest()
        request.method = 'GET'
        request._body = json.dumps(self.new_ad_json)
        response = create_advertisement(request)
        self.assertEqual(response.status_code, 405)

    def test_sunny_advertisement_creation(self):
        request = HttpRequest()
        request.method = 'POST'
        request._body = json.dumps(self.new_ad_json)

        response = create_advertisement(request)
        self.assertEqual(response.status_code, 201)

        bob = User.objects.get(username="Bob")
        porche = Manufacturer.objects.get(name="Porche")
        carrera = Car.objects.get(manufacturer=porche, model="911 Carrera")
        advertisement = Advertisement.objects.get(seller=bob, car=carrera)

    def test_rainy_advertisement_creation_with_missing_attributes(self):
        request = HttpRequest()
        request.method = 'POST'
        bad_ad_json = self.new_ad_json.copy()
        del bad_ad_json['username']
        request._body = json.dumps(bad_ad_json)

        response = create_advertisement(request)
        self.assertEqual(response.status_code, 400)
