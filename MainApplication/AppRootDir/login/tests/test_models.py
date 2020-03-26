from django.test import TestCase
from login.models import User


# Create your tests here.
class UserModelTes(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all tests methods
        User.objects.create(name='ECE651', first_name ='651', last_name = 'ece', password='123456',
                            email='ece651@uwaterloo.ca', catagory = 'customer', c_time='2020-02-01 20:49:28.273716 ')

    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')


    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("name").max_length
        self.assertEquals(max_length, 128)

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')


    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("first_name").max_length
        self.assertEquals(max_length, 128)

    def test_last_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')


    def test_last_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("last_name").max_length
        self.assertEquals(max_length, 128)


    def test_password_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_password_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("password").max_length
        self.assertEquals(max_length, 256)

    def test_catagory_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('catagory').verbose_name
        self.assertEquals(field_label, 'catagory')

    def test_catagory_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("catagory").max_length
        self.assertEquals(max_length, 64)

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
