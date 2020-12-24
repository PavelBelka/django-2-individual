from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Purchase, Car, Equipment
from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTests(TestCase):
    def test_no_products(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['cars'], [])

class PurchaseTest(TestCase):
    def test_no_purchase(self):
        response = self.client.get(reverse('mypurchase'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['purchase'], [])

class ConfigTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='testemail@test.ru'
        )
        Car.objects.create(
            id=1,
            name='tiguan',
            manufacturer = 'testman',
            count=100
        )
        Equipment.objects.create(
            id=1,
            name='test',
            description='testsdescr',
            cost=800000,
            car_id=1
        )
    def test_no_configuration(self):
        response = self.client.get("/configurator/1/0/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['Compl'], 1)

class BuyTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='testemail@test.ru'
        )
        Car.objects.create(
            id=1,
            name='tiguan',
            manufacturer = 'testman',
            count=100
        )
    def test_no_buy(self):
        response = self.client.get("/buy/1/100000")
        self.assertEqual(response.status_code, 200)
        buy = Purchase.objects.all()
        self.assertEqual(buy.count(), 1)

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        User.objects.create_user(**self.credentials)
    def test_login(self):
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

class RegisterTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'email':'testuser@mail.ru',
            'password1': '400120Pav98',
            'password2': '400120Pav98'
        }
    def test_registration(self):
        response = self.client.post(reverse('register'), self.credentials)
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)



