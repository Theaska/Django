from django.db import models
from django.template.defaultfilters import slugify

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.SlugField(unique=True)

    def __str__(self):
        return "Name: %s tagline: %s" % (self.name, self.tagline)

    def save(self, *args, **kwargs):
        self.tagline = slugify(self.tagline)
        super(Blog, self).save(*args, **kwargs)


class Author(models.Model):
    nickname = models.CharField(max_length=50, primary_key=True, unique=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Nickname: {self.nickname}, Email: {self.email}"


class Post(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_publish = models.DateField()
    in_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title}, date: {self.date_publish}, authors: {self.authors}"


class Comment(models.Model):
    author_nickname = models.CharField(max_length=100, blank=False, default=None)
    text = models.TextField()
    date_publish = models.DateTimeField()
    in_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text[:30]










