from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=300, blank=True)
    profile_photo = models.ImageField(upload_to="profile.html", default="static/img")


class Author(models.Model):
    pass


class Book(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='static/images')
   #author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Login(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=18)


class Post(models.Model):
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



