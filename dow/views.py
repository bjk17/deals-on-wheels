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

    required_attributes = ['username', 'manufacturer', 'model', 'registration_number', 'color', 'driven', 'year',
                           'image_url', 'price']
    for attr in required_attributes:
        if attr not in request.POST:
            # 400 Bad Request
            return HttpResponse(status=400)

    user, created = User.objects.get_or_create(
        username=request.POST.get('username'),
        password='password',
        email='{}@example.org'.format(request.POST.get('username'))
    )
    manufacturer, created = Manufacturer.objects.get_or_create(
        name=request.POST.get('manufacturer'),
        description=""
    )
    car, created = Car.objects.get_or_create(
        manufacturer=manufacturer,
        model=request.POST.get('model'),
        registration_number=request.POST.get('registration_number'),
        color=request.POST.get('color'),
        driven=request.POST.get('driven'),
        year=request.POST.get('year'),
        weight=request.POST.get('weight', None),
        registered_at=request.POST.get('registered_at', None),
        next_check=request.POST.get('next_check', None),
        pollution=request.POST.get('pollution', None)
    )
    advertisement, created = Advertisement.objects.get_or_create(
        seller=user,
        car=car,
        image_url=request.POST.get('image_url'),
        price=request.POST.get('price'),
        description=request.POST.get('description', None)
    )

    # 201 Created
    return HttpResponse(status=201)
