from django.test import TestCase
from django.contrib.auth.models import User
from dow.models import Manufacturer, Car, Advertisement


class ModelsTests(TestCase):
    def populate_db_woth_mock_test_data(self):
        alice, created = User.objects.get_or_create(
            username='Alice',
            password='Alice',
            email='alice@example.org'
        )
        ferrari, created = Manufacturer.objects.get_or_create(
            name='Ferrari',
            description='Italian luxury sports car manufacturer'
        )
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
            currency='BTC'
        )
        return alice, ferrari, ferrari_f50, ad_ferrari_f50

    def test_user(self):
        alice, ferrari, ferrari_f50, ad_ferrari_f50 = self.populate_db_woth_mock_test_data()
        user_search = User.objects.get(username='Alice')
        self.assertIsInstance(user_search, User)
        self.assertEqual('alice@example.org', user_search.email)
        self.assertEqual(alice, user_search)

    def test_manufacturer(self):
        alice, ferrari, ferrari_f50, ad_ferrari_f50 = self.populate_db_woth_mock_test_data()
        manufacturer_search = Manufacturer.objects.get(name='Ferrari')
        self.assertIsInstance(manufacturer_search, Manufacturer)
        self.assertEqual('Italian luxury sports car manufacturer', manufacturer_search.description)
        self.assertEqual(ferrari, manufacturer_search)

    def test_car(self):
        alice, ferrari, ferrari_f50, ad_ferrari_f50 = self.populate_db_woth_mock_test_data()
        car_search = Car.objects.get(manufacturer=ferrari, model="F50")
        self.assertIsInstance(car_search, Car)
        self.assertEqual('red', car_search.color)
        self.assertEqual(ferrari_f50, car_search)

    def test_advertisement(self):
        alice, ferrari, ferrari_f50, ad_ferrari_f50 = self.populate_db_woth_mock_test_data()
        advertisement_search = Advertisement.objects.get(seller=alice, car=ferrari_f50)
        self.assertIsInstance(advertisement_search, Advertisement)
        self.assertEqual(15, advertisement_search.price)
        self.assertEqual('BTC', advertisement_search.currency)
        self.assertEqual(ad_ferrari_f50, advertisement_search)
