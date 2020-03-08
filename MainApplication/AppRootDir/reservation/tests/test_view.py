from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from login.models import User
from reservation.models import Table, Reservation

class reserveViewTest(TestCase):

    def setUp(self):
        user1 = User.objects.create(name='ece651', password=hash_code('ece651'), email='ece651@uwaterloo.ca')
        user1.save()
        table1= Table.objects.create(table_id = 1, cap=4, ocupied=True)
        table2= Table.objects.create(table_id = 2, cap=8)
        table1.save()
        table2.save()
        rsv1 = Reservation.objects.create(rsv_number = 1, table_id = 1, no_of_guests = 3, user='ece651', date='2020-5-2')
        rsv1.save()

    def test_object_created(self):
        a = User.objects.get(name='ece651')
        b = Table.objects.get(table_id=1)
        c = Table.objects.get(table_id=2)
        d = Reservation.objects.get(rsv_number=1)
        self.assertEqual(a.password, hash_code('ece651')) 

#get
    def test_view_booktable(self):
        response = self.client.get(reverse('booktable'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation/booktable.html')


#post
    def test_view_booktable_success(self):
        session = self.client.session
        session['is_login'] = True
        session['user_name'] = 'ece651'
        session.save()
        response = self.client.post(reverse('booktable'),{'no_of_guests': 2, 'bookdate':'2020-5-1'})
        new = Reservation.objects.get(table_id=2)
        self.assertEqual(new.rsv_number, 2)
        self.assertRedirects(response,reverse('booksuccess'))


    #def test_view_booktable_not_logged_in(self):
        #response = 




    def test_view_booksuccess(self):
        response = self.client.get(reverse('booksuccess'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation/booksuccess.html')

    def test_view_checkrev(self):
        response = self.client.get(reverse('checkrev'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation/checkrev.html')        
