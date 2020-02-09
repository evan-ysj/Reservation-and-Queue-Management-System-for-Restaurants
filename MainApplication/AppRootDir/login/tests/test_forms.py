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
                "Username/Email": "Harold",
                "password": "123456qubit"
            }
        )
        #                                form.save()
        # print(form.errors)
        self.assertTrue(form.is_valid())

    def test_RegisterForm_valid(self):
        form = RegisterForm(
            data={
                "username": "harold",
                "first_name": "Harold",
                "last_name": "Shi",
                "password1": "123456qubit",
                "password2": "123456qubit",
                "email": "j85shi@uwaterloo.ca"
            }
        )
        #                                form.save()
        # print(form.errors)
        self.assertTrue(form.is_valid())

    def test_RegisterForm_invalid(self):
        form = RegisterForm(
            data={
                "username": "harold",
                "last_name": "Shi",
                "password1": "123456qubit",
                "password2": "123456qubit",
                "email": "j85shi@uwaterloo.ca"
            }
        )
        #                                form.save()
        # print(form.errors)
        self.assertFalse(form.is_valid())

