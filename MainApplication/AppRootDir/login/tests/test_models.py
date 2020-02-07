from django.test import TestCase
from login.models import User


# Create your tests here.
class UserModelTes(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(name='Harold', password='123456qubit', email='j85shi@uwaterloo.ca', c_time='2020-02-01 '
                                                                                                       '20:49:28.273716 ')

    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("name").max_length
        self.assertEquals(max_length, 128)

    def test_password_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_password_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("password").max_length
        self.assertEquals(max_length, 256)

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_c_time_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('c_time').verbose_name
        self.assertEquals(field_label, 'c time')

    def test_object_name_is_name(self):
        user = User.objects.get(id=1)
        expected_object_name = f"{user.name}"
        self.assertEquals(expected_object_name, str(user))
