from django.http import HttpResponse
from django.core import serializers
from dow.models import Manufacturer, Car, Advertisement


def index(request):
    return HttpResponse('<h1>Deals on Wheels</h1> <p>Welcome to site!</p>')


def all_manufacturers_json(request):
    all_manufacturers = Manufacturer.objects.all()
    data = serializers.serialize('json', all_manufacturers)
    return HttpResponse(data, content_type="application/json")


def all_cars_json(request):
    all_cars = Car.objects.all()
    data = serializers.serialize('json', all_cars)
    return HttpResponse(data, content_type="application/json")


def all_advertisements_json(request):
    all_advertisements = Advertisement.objects.all()
    data = serializers.serialize('json', all_advertisements)
    return HttpResponse(data, content_type="application/json")
