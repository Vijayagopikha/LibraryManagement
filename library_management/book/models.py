from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models


from datetime import timedelta
from django.utils import timezone

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
    online_book_url = models.URLField(max_length=200, blank=True, null=True)  # Default is NULL if not set

def __str__(self):
        return self.book_name

class GeneralBook(models.Model):
    category = models.CharField(max_length = 100)
    book_name = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    book_available = models.IntegerField()
    image_url = models.CharField(max_length=100)
    online_book_url = models.URLField(max_length=200, blank=True, null=True)  # Default is NULL if not set


def __str__(self):
     return self.book_name


class BorrowedBook(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    book_type = models.CharField(max_length=50)  # 'technical' or 'general'
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True)  # Make it nullable initially

    def save(self, *args, **kwargs):
        if not self.due_date:
            # Set the due_date to 9 days after borrow_date
            self.due_date = self.borrow_date + timedelta(days=9)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book_name} borrowed by {self.user.username}"
