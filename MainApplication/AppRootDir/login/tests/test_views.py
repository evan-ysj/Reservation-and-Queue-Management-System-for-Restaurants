from django.test import TestCase, Client
from django.urls import reverse
from login.models import User
from django.contrib.auth.models import User



class loginViewTest(TestCase):

    def setUp(self):
        # user1 = User.objects.create_user(username='ece651', password='ece651', email='ece651@uwaterloo.ca', c_time='2020-02-01 '
        #                                                                                             '20:49:28.273716 ')
        user1 = User.objects.create(name='ece651', password='ece651', email='ece651@uwaterloo.ca', c_time='2020-02-01 '
                                                                                                    '20:49:28.273716 ')
        user1.save()
    def test_view_index_url_exists(self):
        response = self.client.get('/login/index/')
        self.assertEqual(response.status_code, 200)

    def test_view_index_correct_template(self):
        response = self.client.get(reverse('index'))
        # response = self.client.get('/login/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/index.html')

    def test_view_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(response.url.startswith('/accounts/login/'))
        self.assertTemplateUsed(response, 'login/login.html')

    # def test_view_loged_in_redirect_index(self):
    #     logged_in = self.client.login(username='ece650', password="ece651")
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertTrue(response.url.startswith('/accounts/login/'))
    #     self.assertTemplateUsed(response, 'login/login.html')
