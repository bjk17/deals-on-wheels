from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from dow.models import Manufacturer, Car, Advertisement
import json


def index(request):
    return HttpResponse('<h1>Deals on Wheels</h1> <p>Welcome to site!</p>')


def all_manufacturers_json(request):
    all_manufacturers = Manufacturer.objects.all()
    data = serializers.serialize('json', all_manufacturers, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(data, content_type="application/json")


def all_cars_json(request):
    all_cars = Car.objects.all()
    data = serializers.serialize('json', all_cars, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(data, content_type="application/json")


def all_advertisements_json(request):
    all_advertisements = Advertisement.objects.all()
    data = serializers.serialize('json', all_advertisements, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(data, content_type="application/json")


def create_advertisement(request):
    if request.method != 'POST':
        # 405 Method Not Allowed
        return HttpResponse(status=405)

    json_object = json.loads(request.POST)

    user, created = User.objects.get_or_create(
        username = json_object.get('username', 'SecretUser'),
        password = 'password',
        email = '{}@example.org'.format(json_object.get('username', 'SecretUser'))
    )
    manufacturer, created = Manufacturer.objects.get_or_create(
        name = json_object.get('manufacturer', None),
        description = ""
    )
    car, created = Car.objects.get_or_create(
        manufacturer = manufacturer,
        model = json_object.get('model', None),
        registration_number = json_object.get('registration_number', None),
        color = json_object.get('color', None),
        driven = json_object.get('driven', None),
        year = json_object.get('year', None),
        weight = json_object.get('weight', None),
        registered_at = json_object.get('registered_at', None),
        next_check = json_object.get('next_check', None),
        pollution = json_object.get('pollution', None)
    )
    advertisement, created = Advertisement.objects.get_or_create(
        seller = user,
        car = car,
        image_url = json_object.get('image_url', None),
        price = json_object.get('price', None),
        description = json_object.get('description', None)
    )

    # Return a "created" (201) response code.
    return HttpResponse(status=201)

