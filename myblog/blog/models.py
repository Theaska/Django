from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    nickname = models.CharField(max_length=50, primary_key=True, unique=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Nickname: {self.nickname}, Email: {self.email}"


class Post(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=400)
    date_publish = models.DateField()
    in_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title}, date: {self.date_publish}"


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_publish = models.DateField()
    in_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text[:30]










