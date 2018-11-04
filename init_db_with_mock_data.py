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
    image_url="https://www.supercars.net/blog/wp-content/uploads/2016/05/ferrari_f50_preserial_red_front_view_100209_1920x1080.jpg",
    price=15,
    currency='BTC'
)

# Toyota Corolla
toyota_corolla, created = Car.objects.get_or_create(
    manufacturer=toyota,
    model="Corolla",
    color="White",
    driven=0,
    year=2018
)
ad_toyota_corolla, created = Advertisement.objects.get_or_create(
    seller=alice,
    car=toyota_corolla,
    image_url="https://upload.wikimedia.org/wikipedia/commons/d/dd/2018_Toyota_Corolla_%28ZRE172R%29_Ascent_sedan_%282018-08-27%29.jpg",
    price=3990000,
    currency='ISK',
    description="100% NEW -- has never been used!"
)

# Toyota Hilux
toyota_hilux, created = Car.objects.get_or_create(
    manufacturer=toyota,
    model="Hilux",
    color="blue",
    driven=85400,
    year=2016
)
ad_toyota_hilux, created = Advertisement.objects.get_or_create(
    seller=alice,
    car=toyota_hilux,
    image_url="http://wallpapersqq.net/wp-content/uploads/2016/04/toyota-hilux-2016-blue-new-2016-picture.jpg",
    price=1590000,
    currency='ISK'
)
