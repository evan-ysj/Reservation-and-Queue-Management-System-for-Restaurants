from django.test import TestCase, Client, RequestFactory
from waitlist.forms import TakenoForm, CheckstateForm
from django.shortcuts import render, redirect
from django.urls import reverse
from waitlist.models import Waitlist
from reservation.models import Table, Reservation

class waitlistViewTest(TestCase):

    def setUp(self):
        wait = Waitlist.objects.create(id=1, guests=3, lastname='xu', catagory='a')
        wait.save()

    def test_object_created(self):
        a = Waitlist.objects.get(lastname='xu')
        self.assertEqual(a.id, 1)

#get
    def test_view_takeno(self):
        response = self.client.get(reverse('takeno'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'takeno.html')

#post
    def test_view_takeno_success(self):
        response = self.client.post(reverse('takeno'),{'no_of_guests': 2, 'name':'chen'})
        self.assertRedirects(response,reverse('takesuccess'))

    def test_view_takeno_fail(self):
        response = self.client.post(reverse('takeno'),{'no_of_guests': 'b', 'name':'chen'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'takeno.html')
        #self.assertEqual(response.context['message'], "Sorry, something went wrong. Please try again!")

#get
    def test_view_takesuccess(self):
        session = self.client.session
        session['number'] = 'b34'
        session.save()         
        response = self.client.get(reverse('takesuccess'))
        session.flush()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'takesuccess.html')

    def test_view_takesuccess_not_take(self):
        response = self.client.get(reverse('takesuccess'))
        self.assertRedirects(response, reverse('takeno'))

#get
    def test_view_checkstate_render(self):
        response = self.client.get(reverse('checkstate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkstate.html')

#post
    def test_view_checkstate_success(self):
        response = self.client.post(reverse('checkstate'),{'number': "a1"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkstate.html')
        self.assertEqual(response.context['result'], 0)

    def test_view_checkstate_invalid_number(self):
        response = self.client.post(reverse('checkstate'),{'number': "a2"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkstate.html')
        self.assertEqual(response.context['message'], "Invalid number!")

    def test_view_checkstate_invalid_number2(self):
        response = self.client.post(reverse('checkstate'),{'number': "a"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkstate.html')
        self.assertEqual(response.context['message'], "Invalid number!")

