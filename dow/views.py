from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from dow.models import Manufacturer, Car, Advertisement
import json


def index(request):
    return HttpResponse('<h1>Deals on Wheels</h1> <p>Welcome to site!</p>')


def all_manufacturers_json(request):
    all_manufacturers = Manufacturer.objects.all()
    data = serializers.serialize('json', all_manufacturers, use_natural_foreign_keys=True,
                                 use_natural_primary_keys=True)
    return HttpResponse(data, content_type="application/json")


def all_cars_json(request):
    all_cars = Car.objects.all()
    data = serializers.serialize('json', all_cars, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(data, content_type="application/json")


def all_advertisements_json(request):
    all_advertisements = Advertisement.objects.all()
    data = serializers.serialize('json', all_advertisements, use_natural_foreign_keys=True,
                                 use_natural_primary_keys=True)
    return HttpResponse(data, content_type="application/json")


def create_advertisement(request):
    if request.method != 'POST':
        # 405 Method Not Allowed
        return HttpResponse(status=405)

    body_json = json.loads(request.body)

    required_attributes = ['username', 'manufacturer', 'model', 'registration_number', 'color', 'year', 'image_url',
                           'price']
    for attr in required_attributes:
        if attr not in body_json:
            # 400 Bad Request
            return HttpResponse(status=400)

    user, created = User.objects.get_or_create(
        username=str(body_json.get('username')),
        password='password',
        email="{}@example.org".format(str(body_json.get('username')))
    )
    manufacturer, created = Manufacturer.objects.get_or_create(
        name=body_json.get('manufacturer'),
        description=""
    )
    car, created = Car.objects.get_or_create(
        manufacturer=manufacturer,
        model=body_json.get('model'),
        registration_number=body_json.get('registration_number'),
        color=body_json.get('color'),
        driven=body_json.get('driven'),
        year=body_json.get('year'),
        weight=body_json.get('weight', None),
        registered_at=body_json.get('registered_at', None),
        next_check=body_json.get('next_check', None),
        pollution=body_json.get('pollution', None)
    )
    advertisement, created = Advertisement.objects.get_or_create(
        seller=user,
        car=car,
        image_url=body_json.get('image_url'),
        price=body_json.get('price'),
        description=body_json.get('description', None)
    )

    # 201 Created
    return HttpResponse(status=201)
