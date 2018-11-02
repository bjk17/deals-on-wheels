from django.contrib.auth.models import User
from dow.models import Manufacturer, Car, Advertisement

User.objects.filter(username='admin').delete()
User.objects.create_superuser(
    username='admin',
    password='admin',
    email='admin@example.org'
)

alice, created = User.objects.get_or_create(
    username='Alice',
    password='Alice',
    email='alice@example.org'
)

ferrari, created = Manufacturer.objects.get_or_create(
    name='Ferrari',
    description='Italian luxury sports car manufacturer'
)

toyota, created = Manufacturer.objects.get_or_create(
    name='Toyota',
    description='Japanese value brand car manufacturer'
)

# Ferrari F50
ferrari_f50, created = Car.objects.get_or_create(
    manufacturer=ferrari,
    model="F50",
    color="red",
    driven=33000,
    year=1995
)
ad_ferrari_f50, created = Advertisement.objects.get_or_create(
    seller=alice,
    car=ferrari_f50,
    price=10000000
)

# Toyota Corolla
toyota_corolla, created = Car.objects.get_or_create(
    manufacturer=toyota,
    model="Corolla",
    color="White",
    driven=0,
    year=2019
)
ad_toyota_corolla, created = Advertisement.objects.get_or_create(
    seller=alice,
    car=toyota_corolla,
    price=3990000
)

# Toyota Hilux
toyota_hilux, created = Car.objects.get_or_create(
    manufacturer=toyota,
    model="Hilux",
    color="blue",
    driven=85400,
    year=2001
)
ad_toyota_hilux, created = Advertisement.objects.get_or_create(
    seller=alice,
    car=toyota_hilux,
    price=590000
)
