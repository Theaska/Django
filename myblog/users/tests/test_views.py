from django.test import TestCase, Client
from blog.models import Blog, Author, Post, Comment
from users.models import CustomUser
from django.urls import reverse

class TestSignupView(TestCase):

    def test_signup_without_login(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign up')
        self.assertContains(response, 'form')

    def test_signup_with_login(self):
        user = CustomUser.objects.create_user(username='User', email='user@mail.ru', password='1234qwe')
        client = Client()
        client.login(username='User', password='1234qwe')
        response = client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('myblog:index'))

    def test_signup_with_login_and_follow(self):
        user = CustomUser.objects.create_user(username='User', email='user@mail.ru', password='1234qwe')
        client = Client()
        client.login(username='User', password='1234qwe')
        response = client.get(reverse('users:signup'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('myblog:index'))
        self.assertContains(response, 'Welcome, %s' % user.username)


class TestLoginView(TestCase):

    def test_login_when_not_login(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Login with Gmail')
    
    def test_login_when_login(self):
        user = CustomUser.objects.create_user(username='User', email='user@mail.ru', password='1234qwe')
        client = Client()
        client.login(username='User', password='1234qwe')
        response = client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('myblog:index'))


class TestLogoutView(TestCase):

    def test_logout_without_login(self):
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('myblog:index'))

    def test_logout_with_login(self):
        user = CustomUser(username='user', email='email@mail.ru', password='123qwe')
        client = Client()
        client.login(username='user', password = '123qwe')
        response = client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('myblog:index'))