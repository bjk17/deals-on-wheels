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
    registration_number="AB123",
    color="red",
    driven=33000,
    year=1995
)
ad_ferrari_f50, created = Advertisement.objects.get_or_create(
    seller=alice,
    car=ferrari_f50,
    image_url="https://www.supercars.net/blog/wp-content/uploads/2016/05/ferrari_f50_preserial_red_front_view_100209_1920x1080.jpg",
    price=15,
    currency='BTC',
    description="Car for winners. Be a winner. Have a Ferrari F50. Be admired. Be an alpha. Be cool. Be chill. Drive safely."
)

# Toyota Corolla
toyota_corolla, created = Car.objects.get_or_create(
    manufacturer=toyota,
    model="Corolla",
    registration_number="CD456",
    color="White",
    driven=0,
    year=2018,
    weight=2345
)
ad_toyota_corolla, created = Advertisement.objects.get_or_create(
    seller=alice,
    car=toyota_corolla,
    image_url="https://upload.wikimedia.org/wikipedia/commons/d/dd/2018_Toyota_Corolla_%28ZRE172R%29_Ascent_sedan_%282018-08-27%29.jpg",
    price=3990000,
    currency='ISK',
    description="100% NEW -- has never been used! A really, really good car. It uses very little gasoline and doesn't make much sound."
)

# Toyota Hilux
toyota_hilux, created = Car.objects.get_or_create(
    manufacturer=toyota,
    model="Hilux",
    registration_number="EF789",
    color="blue",
    driven=85400,
    year=2016,
    weight=3456
)
ad_toyota_hilux, created = Advertisement.objects.get_or_create(
    seller=alice,
    car=toyota_hilux,
    image_url="http://wallpapersqq.net/wp-content/uploads/2016/04/toyota-hilux-2016-blue-new-2016-picture.jpg",
    price=1590000,
    currency='ISK',
    description="Chrashed it once when doing coke with my stripper girlfriend but the cop came and was very understanding so I slept it off at the station (girlfriend left me that night) and paid a small fine the day after. Me and the cop are best friends now."
)
