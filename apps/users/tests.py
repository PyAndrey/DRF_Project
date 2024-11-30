# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User


class UserTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))
