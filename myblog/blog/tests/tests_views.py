from django.test import TestCase, Client
from blog.models import Post, Author, Blog, Comment
from django.utils import timezone
import datetime as dt
from django.urls import reverse
from users.models import CustomUser
from blog.forms import FormComment

class IndexViewTest(TestCase):

    def test_index_with_no_posts(self):
        response = self.client.get(reverse('myblog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no posts in the blog.')
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_index_with_future_post(self):
        blog = Blog.objects.create(name='name', tagline='name')
        author = Author.objects.create(nickname='author', email='email@mail.ru')
        post = Post.objects.create(title='title', text='text', date_publish=dt.datetime.strftime(dt.datetime.now() + dt.timedelta(days=10), "%Y-%m-%d"), in_blog=blog)
        post.authors.add(author)
        post.save()
        response = self.client.get(reverse('myblog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no posts in the blog.')
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_index_with_post(self):
        blog = Blog.objects.create(name='name', tagline='name')
        author = Author.objects.create(nickname='author', email='email@mail.ru')
        post = Post.objects.create(title='title', text='text', date_publish=dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d"), in_blog=blog)
        post.authors.add(author)
        post.save()
        response = self.client.get(reverse('myblog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], [post], transform=lambda x: x)


class PostViewTest(TestCase):
    
    def create_post(self):
        author = Author.objects.create(nickname='Author', email='email@email.com')
        blog = Blog.objects.create(name='Blog', tagline='tag')
        post = Post.objects.create(title='title', text='text', date_publish=dt.datetime.now(), in_blog=blog)
        post.authors.add(author)
        return [author, blog, post]

    def test_no_login_no_comment_form(self):
        author, blog, post = self.create_post()
        response = self.client.get(reverse('myblog:post', args=(post.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Comments only for authorized users')
        
    def test_no_login_no_access_to_post_comment(self):
        author, blog, post = self.create_post()
        response = self.client.post(reverse('myblog:post', args=(post.id,)))
        self.assertEqual(response.status_code, 302)
    
    def test_comment_form(self):
        author, blog, post = self.create_post()
        user = CustomUser.objects.create_user(username='User', email='user@mail.ru', password='1234qwe')
        client = Client()
        client.login(username='User', password='1234qwe')
        response = client.get(reverse('myblog:post', args=(post.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')
        
    def test_post_comment(self):
        author, blog, post = self.create_post()
        user = CustomUser.objects.create_user(username='User', email='user@mail.ru', password='1234qwe')
        client = Client()
        client.login(username='User', password='1234qwe')
        text_comment = 'Comment comment'
        response = client.post(reverse('myblog:post', args=(post.id,)), {'text': text_comment})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('myblog:post', args=(post.id,)))
        response = client.get(reverse('myblog:post', args=(post.id,)))
        self.assertContains(response, text_comment)

class TestMonthArchiveView(TestCase):

    def test_no_posts_in_archive(self):
        response = self.client.get(reverse('myblog:archive', args=('may',)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no posts in the archive.')
    
    def test_post_in_archive(self):
        blog = Blog.objects.create(name='name', tagline='name')
        author = Author.objects.create(nickname='author', email='email@mail.ru')
        post = Post.objects.create(title='title', text='text', date_publish="2019-05-23", in_blog=blog)
        post.authors.add(author)
        post.save()
        response = self.client.get(reverse('myblog:archive', args=('may',)))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [post], transform=lambda x:x)
