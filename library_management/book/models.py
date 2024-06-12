from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class Signup(models.Model):
     username = models.CharField(max_length = 100)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length = 100)
     confirm_password = models.CharField(max_length=100)
     isadmin = models.BooleanField(default=False)

def __str__(self):
     return self.username

class TechnicalBook(models.Model):
    departname = models.CharField(max_length=100)
    book_name = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    edition = models.CharField(max_length = 100)
    book_available = models.IntegerField()
    image_url = models.CharField(max_length=100)

def __str__(self):
        return self.book_name

class GeneralBook(models.Model):
    category = models.CharField(max_length = 100)
    book_name = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    book_available = models.IntegerField()
    image_url = models.CharField(max_length=100)

def __str__(self):
     return self.book_name


