from django.test import TestCase, Client
from django.urls import reverse
from login.models import User
from reservation.models import Table, Reservation
from waitlist.models import Waitlist
from login.views import hash_code

class IntegrationTest(TestCase):

    def setUp(self):
        user1 = User.objects.create(name='ece651', password=hash_code('ece651'), email='ece651@uwaterloo.ca')
        user1.save()
        table1= Table.objects.create(table_id = 1, cap=4)
        table2= Table.objects.create(table_id = 2, cap=8)
        table1.save()
        table2.save()
        rsv1 = Reservation.objects.create(rsv_number = 1, table_id = table1, no_of_guests = 3, user='ece651', date='2020-5-1')
        rsv1.save()
        wait1 = Waitlist.objects.create(id=0, guests=3, lastname='xu', catagory='a')
        wait1.save()

    def test_integration_setup_success(self):
        #raise DoesNotExist error if failed
        a = User.objects.get(name='ece651', password=hash_code('ece651'), email='ece651@uwaterloo.ca')
        b = Table.objects.get(table_id = 1, cap=4)
        c = Table.objects.get(table_id = 2, cap=8)
        d = Waitlist.objects.get(id=0, guests=3, lastname='xu', catagory='a')
        e = Reservation.objects.get(rsv_number = 1, table_id = b, no_of_guests = 3, user='ece651', date='2020-5-1')
        
    def test_integration_frontend_login_book_chkrsv(self):
        response = self.client.post(reverse('login'),{'username':'ece651', 'password':'ece651'})
        self.assertEqual(User.objects.get(name='ece651').password, hash_code('ece651'))
        self.assertRedirects(response,reverse('index'))

        response = self.client.get(reverse('booktable'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booktable.html')

        response = self.client.post(reverse('booktable'),{'no_of_guests': 2, 'bookdate':'2020-5-2'})
        new = Reservation.objects.filter(user = 'ece651').count()
        self.assertEqual(new, 2)
        self.assertRedirects(response,reverse('booksuccess'))

        response = self.client.get(reverse('booksuccess'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booksuccess.html')

        response = self.client.get(reverse('checkrev'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkrev.html')

        
    def test_integration_frontend_register_login_chpasswd_logout(self):
        response = self.client.post(reverse('register'), {'username':'newuser','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678', 'email':'fake@uwaterloo.ca'})
        self.assertTrue('is_login' not in self.client.session)
        self.assertRedirects(response,reverse('login'))
        
        response = self.client.post(reverse('login'),{'username':'newuser', 'password':'12345678'})
        self.assertRedirects(response,reverse('index'))

        response = self.client.post(reverse('chpasswd'), {'password':'12345678', 'password1':'87654321', 'password2':'87654321'})
        self.assertEqual(User.objects.get(name='newuser').password, hash_code('87654321'))
        self.assertRedirects(response, reverse('chpasswdsuccess'))


    def test_integration_frontend_login_profile_deluser(self):
        response = self.client.post(reverse('login'),{'username':'ece651', 'password':'ece651'})
        self.assertEqual(User.objects.get(name='ece651').password, hash_code('ece651'))
        self.assertRedirects(response,reverse('index'))
                             
        response = self.client.get(reverse('profile')) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/profile.html')

        response = self.client.get(reverse('deleteuser'))
        try:
            a=User.objects.get(name='ece651')
        except:
            pass
        else:
            raise NameError("fail to delete")
        self.assertRedirects(response,reverse('index'))
        
    def test_integration_frontend_takeno_takesuccess_chkstate(self):
        response = self.client.post(reverse('takeno'),{'no_of_guests': 2, 'name':'chen'})
        self.assertRedirects(response,reverse('takesuccess'))

        response = self.client.get(reverse('takesuccess'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'takesuccess.html')

        response = self.client.get(reverse('checkstate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkstate.html')

        response = self.client.post(reverse('checkstate'),{'number': self.client.session['number'], 'name':'chen'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkstate.html')
        self.assertEqual(response.context['result'], 1)
                                   
    def test_integration_backend(self):
# autonatical change of table state is not implemented
        response = self.client.get(reverse('change_table'),{'table_id': 1, 'occupied': 'False'})
        self.assertRedirects(response,reverse('managetb'))

        response = self.client.get(reverse('managetb'))
        self.assertEqual(Table.objects.get(table_id=1).occupied, True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/managetb.html')
               
#    def test_integration_frontback_interaction_rsv(self):
# cancelling reservation is not implemented

    def test_integration_frontback_interaction_waitlist(self):   
# frontend  
        response = self.client.post(reverse('takeno'),{'no_of_guests': 3, 'name':'lu'})
        waitlist_number = self.client.session['number']
        self.assertRedirects(response,reverse('takesuccess')) 
# backend
        response = self.client.get(reverse('managewl'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'login/managewl.html')

        response = self.client.get(reverse('pop_waitlist'),{'id': 0})
        self.assertRedirects(response,reverse('managewl'))
#frontend
        response = self.client.post(reverse('checkstate'),{'number': waitlist_number})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkstate.html')
        self.assertEqual(response.context['result'], 0)


        
