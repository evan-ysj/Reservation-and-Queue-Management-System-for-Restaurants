from django.test import TestCase
from login.forms import *
from login.models import *
from django.test import Client
import datetime
from django.utils import timezone


class User_Form_Register_Form_Test(TestCase):
    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(
            data={
                "username": "Harold",
                "password": "123456qubit"
            }
        )
        #                                form.save()

        self.assertTrue(form.is_valid())

    def test_RegisterForm_valid(self):
        form = RegisterForm(
            data={
                "username": "harold",
                "firstname": "Harold",
                "lastname": "Shi",
                "password1": "123456qubit",
                "password2": "123456qubit",
                "email": "j85shi@uwaterloo.ca"
            }
        )
        self.assertTrue(form.is_valid())

    def test_RegisterForm_miss_fields(self):
        form = RegisterForm(
            data={
                "username": "harold",
                "lastname": "Shi",
                "password1": "123456qubit",
                "password2": "123456qubit",
                "email": "j85shi@uwaterloo.ca"
            }
        )
        self.assertFalse(form.is_valid())

#    def test_RegisterForm_extra_fields(self):
#        form = RegisterForm(
#            data={
#                "username": "harold",
#                "firstname": "Harold",
#                "lastname": "Shi",
#                "password1": "123456qubit",
#                "password2": "123456qubit",
#                "email": "j85shi@uwaterloo.ca",
#                "extra": "extra"
#            }
#        )
#        self.assertFalse(form.is_valid())
