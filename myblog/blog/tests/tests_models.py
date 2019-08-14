from django.test import TestCase
from blog.models import Blog, Author, Post, Comment
from django.db.utils import IntegrityError

class TestBlogModel(TestCase):

    def test_create_not_slug_tagline(self):
        blog = Blog.objects.create(name='Blog1', tagline='not slug tagline')
        self.assertEqual(blog.tagline, 'not-slug-tagline')


class TestAuthorModel(TestCase):

    def test_not_unique_nickname(self):
        Author.objects.create(nickname='auth', email='mail')
        with self.assertRaises(IntegrityError):
            Author.objects.create(nickname='auth', email='mail')


class TestCommentModel(TestCase):

    def test_comment_without_author_nickname(self):
        blog = Blog(name='name', tagline='tagline')
        blog.save()
        post = Post(title='title', text='text', date_publish='2019-03-23', in_blog= blog)
        post.save()
        with self.assertRaises(IntegrityError):
            Comment.objects.create(text='comment', date_publish='2019-03-23 15:32', in_post=post)
            