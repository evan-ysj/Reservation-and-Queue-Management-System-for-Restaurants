from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from login.models import User
import hashlib

class loginViewTest(TestCase):

    def setUp(self):
        user1 = User.objects.create(name='ece651', password=hash_code('ece651'), email='ece651@uwaterloo.ca')
        user1.save()

    def test_user_created(self):
        a = User.objects.get(name='ece651')
        self.assertEqual(a.password, hash_code('ece651'))
#tests get
    def test_view_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/index.html')

#tests get
    def test_view_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')

    def test_view_login_already_logged_in(self):
        session = self.client.session
        session['is_login'] = True
        session.save()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['is_login'], True)
        session.flush()

#tests post
    def test_view_login_name(self):
        response = self.client.post(reverse('login'),{'username':'ece651', 'password':'ece651'})
        self.assertEqual(self.client.session['user_name'], 'ece651')
        self.assertEqual(self.client.session['is_login'], True)
        self.assertRedirects(response,reverse('index'))

    def test_view_login_email(self):
        response = self.client.post(reverse('login'),{'username':'ece651@uwaterloo.ca', 'password':'ece651'})
        self.assertEqual(self.client.session['user_name'], 'ece651')
        self.assertEqual(self.client.session['is_login'], True)
        self.assertRedirects(response,reverse('index'))
        #tests redirect asserthtmlEqual

    def test_view_login_bad_password(self):
        response = self.client.post(reverse('login'),{'username':'ece651@uwaterloo.ca', 'password':'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
        self.assertTrue('is_login' not in self.client.session)
        self.assertEqual(response.context['message'], 'Incorrect password!')
        #check message

    def test_view_login_nonexist_user(self):
        response = self.client.post(reverse('login'),{'username':'baduser', 'password':'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
        self.assertTrue('is_login' not in self.client.session)
        self.assertEqual(response.context['message'], 'Username does not exist!')


#tests get
    def test_view_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/register.html')

    def test_view_register_already_logged_in (self):
        session = self.client.session
        session['is_login'] = True
        session.save()
        response = self.client.get(reverse('register'))
        self.assertRedirects(response,reverse('index'))
        self.assertEqual(self.client.session['is_login'], True)
        session.flush()

#tests post
#    def test_view_register_bad_username(self):
#        response = self.client.post(reverse('register'), {'username':'}}{_{','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678', 'email':'fake@uwaterloo.ca'})
#        self.assertEqual(response.status_code, 200)
#        self.assertTemplateUsed(response, 'login/register.html')

    def test_view_register_password_mismatch(self):
        response = self.client.post(reverse('register'), {'username':'newuser','firstname':'first','lastname':'last','password1':'87654321','password2':'12345678', 'email':'fake@uwaterloo.ca'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/register.html')
        self.assertTrue('is_login' not in self.client.session)
        self.assertEqual(response.context['message'], 'The passwords you entered do not match')

    def test_view_register_same_name_user(self):
        response = self.client.post(reverse('register'), {'username':'ece651','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678', 'email':'fake@uwaterloo.ca'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/register.html')
        self.assertTrue('is_login' not in self.client.session)
        self.assertEqual(response.context['message'], 'Username cannot be used. Please choose another username')


    def test_view_register_same_email_user(self):
        response = self.client.post(reverse('register'), {'username':'newuser','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678', 'email':'ece651@uwaterloo.ca'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/register.html')
        self.assertTrue('is_login' not in self.client.session)
        self.assertEqual(response.context['message'], 'Email address cannot be used. Please choose another email address')

    def test_view_register_success(self):
        response = self.client.post(reverse('register'), {'username':'newuser','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678', 'email':'fake@uwaterloo.ca'})
        self.assertTrue('is_login' not in self.client.session)
        self.assertRedirects(response,reverse('login'))


    def test_view_register_blank(self):
        response = self.client.post(reverse('register'), {'username':'newuser','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678'})

#tests get
    def test_view_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response,reverse('index'))

    def test_view_logout_logged_in(self):
        session = self.client.session
        session['is_login'] = True
        session.save()
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response,reverse('index'))
        self.assertTrue('is_login' not in self.client.session)
        session.flush()

def hash_code(s, salt='ece651'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
