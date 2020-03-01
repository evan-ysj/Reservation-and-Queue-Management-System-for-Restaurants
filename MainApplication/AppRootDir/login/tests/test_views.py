from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from login.models import User
from .views import MyView, my_view

class loginViewTest(TestCase):

    def setUp(self):
		self.factory = RequestFactory()
        self.user1 = User.objects.create(name='ece651', password='ece651', email='ece651@uwaterloo.ca')
        self.user1.save()

#test get
    def test_view_index(self):
        response = self.client.get(reverse('index'))
        # response = self.client.get('/login/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/index.html')

#test get
    def test_view_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
		
	def test_view_login_already_logged_in(self):
		request = self.factory.get(reverse('login'))
		request.session['is_login'] = True
		response = MyView.as_view()(request)
        self.assertRedirects(response,reverse('index'))

#test post
	def test_view_login_name(self):
		response = self.client.post('/login/',{'username':'ece651', 'password':'ece651'})
		self.assertTrue(response.request.session['is_login'])
		self.assertRedirects(response,reverse('index'))
	
	def test_view_login_email(self):
		response = self.client.post('/login/',{'username':'ece651@uwaterloo.ca', 'password':'ece651'})
		self.assertTrue(response.request.session['is_login'])
		self.assertRedirects(response,reverse('index'))
		#rest redirect asserthtmlEqual
	
	def test_view_login_bad_password(self):
		response = self.client.post('/login/',{'username':'ece651@uwaterloo.ca', 'password':'wrongpassword'})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'login/login.html')
		self.assertEuqal(response.request.session['is_login'], None)
		self.assertEqual(response.context[message], 'Incorrect password!')
		#check message
	
	def test_view_login_nonexist_user(self):
		response = self.client.post('/login/',{'username':'baduser', 'password':'wrongpassword'})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'login/login.html')
		self.assertEuqal(response.request.session['is_login'], None)	
		self.assertEqual(response.context[message], 'Username does not exist!')	
	
		
#test get
	def test_view_register(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'login/register.html')
	
	def test_view_register_already_logged_in (self):
		request = self.factory.get(reverse('register'))
		request.session['is_login'] = True
		response = MyView.as_view()(request)
        self.assertRedirects(response,reverse('index'))

#test post	
	#def test_view_register_bad_username(self):
	#is it tested in the models already?
	
	def test_view_register_password_mismatch(self):
		response = self.client.post(reverse('register'), {'username':'newuser','firstname':'first','lastname':'last','password1':'87654321','password2':'12345678', 'email':'fake@uwaterloo.ca'})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'login/register.html')
		self.assertEuqal(response.request.session['is_login'], None)
		self.assertEqual(response.context[message], 'The passwords you entered do not match')
		
	def test_view_register_same_name_user(self):
		response = self.client.post(reverse('register'), {'username':'ece651','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678', 'email':'fake@uwaterloo.ca'})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'login/register.html')
		self.assertEuqal(response.request.session['is_login'], None)
		self.assertEqual(response.context[message], 'Username cannot be used. Please choose another username')
	
	
	def test_view_register_same_email_user(self):
		response = self.client.post(reverse('register'), {'username':'newuser','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678', 'email':'ece651@uwaterloo.ca'})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'login/register.html')
		self.assertEuqal(response.request.session['is_login'], None)
		self.assertEqual(response.context[message], 'Email address cannot be used. Please choose another email address')
	
	def test_view_register_success(self):
		response = self.client.post(reverse('register'), {'username':'newuser','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678', 'email':'fake@uwaterloo.ca'})
		self.assertEuqal(response.request.session['is_login'], None)
		self.assertRedirects(response,reverse('login'))
		
	
	def test_view_register_blank(self):
		response = self.client.post(reverse('register'), {'username':'newuser','firstname':'first','lastname':'last','password1':'12345678','password2':'12345678'})
	
#test get	
	def test_view_logout(self):
		response = self.client.get(reverse('logout'))
		self.assertRedirects(response,reverse('index'))
		
	def test_view_logout_logged_in(self):
		request = self.factory.get(reverse('register'))
		request.session['is_login'] = True
		response = MyView.as_view()(request)
        self.assertRedirects(response,reverse('index'))
		
	def test_view_logout_not_logged_in(self):
		request = self.factory.get(reverse('register'))
		request.session['is_login'] = False
		response = MyView.as_view()(request)
        self.assertRedirects(response,reverse('index'))
