from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from login.models import User
from reservation.models import Table, Reservation
from login.views import hash_code

class reserveViewTest(TestCase):

    def setUp(self):
        user1 = User.objects.create(name='ece651', password=hash_code('ece651'), email='ece651@uwaterloo.ca')
        user1.save()
        table1= Table.objects.create(table_id = 1, cap=4, occupied=True)
        table2= Table.objects.create(table_id = 2, cap=8)
        table1.save()
        table2.save()
        rsv1 = Reservation.objects.create(rsv_number = 1, table_id = table1, no_of_guests = 3, user='ece651', date='2020-5-1')
        rsv1.save()

    def test_object_created(self):
        a = User.objects.get(name='ece651')
        b = Table.objects.get(table_id=1)
        c = Table.objects.get(table_id=2)
        d = Reservation.objects.get(rsv_number=1)
        self.assertEqual(a.password, hash_code('ece651'))

#get
    def test_view_booktable(self):
        session = self.client.session
        session['is_login'] = True
        session.save() 
        response = self.client.get(reverse('booktable'))
        session.flush()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booktable.html')

    def test_view_booktable_not_logged_in(self):
        response = self.client.get(reverse('booktable'))
        self.assertRedirects(response, reverse('login'))

#post
    def test_view_booktable_success(self):
        session = self.client.session
        session['is_login'] = True
        session['user_name'] = 'ece651'
        session.save()
        response = self.client.post(reverse('booktable'),{'no_of_guests': 2, 'bookdate':'2020-5-2'})
        new = Reservation.objects.filter(user = 'ece651').count()
        self.assertEqual(new, 2)
        self.assertRedirects(response,reverse('booksuccess'))
        session.flush()

    def test_view_booktable_bad_date(self):
        session = self.client.session
        session['is_login'] = True
        session['user_name'] = 'ece651'
        session.save()
        response = self.client.post(reverse('booktable'),{'no_of_guests': 2, 'bookdate':'2019-5-2'})
        session.flush()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booktable.html')
        self.assertEqual(response.context['message'], 'Please select a date that is later than today.')  

    def test_view_booktable_duplicate_date(self):
        session = self.client.session
        session['is_login'] = True
        session['user_name'] = 'ece651'
        session.save()
        response = self.client.post(reverse('booktable'),{'no_of_guests': 2, 'bookdate':'2020-5-1'})
        session.flush()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booktable.html')
        self.assertEqual(response.context['message'], 'You have already booked a table on that day. Please pick another date.') 

   
    def test_view_booktable_not_logged_in(self):
        response = self.client.post(reverse('booktable'),{'no_of_guests': 2, 'bookdate':'2020-5-2'})
        self.assertRedirects(response,reverse('login'))


    def test_view_booksuccess(self):
        session = self.client.session
        session['is_login'] = True
        session.save()
        response = self.client.get(reverse('booksuccess'))
        session.flush()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booksuccess.html')

    def test_view_booksuccess_not_logged_in(self):
        response = self.client.get(reverse('booksuccess'))
        self.assertRedirects(response, reverse('login'))

    def test_view_checkrev(self):
        session = self.client.session
        session['is_login'] = True
        session['user_name'] = 'ece651'
        session.save()
        response = self.client.get(reverse('checkrev'))
        session.flush()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkrev.html')

    def test_view_checkrev_not_logged_in(self):
        response = self.client.get(reverse('checkrev'))
        self.assertRedirects(response, reverse('login'))
