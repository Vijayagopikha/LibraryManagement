from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
'''class UserManager(BaseUserManager):
    def create_user(self, email, name, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, username, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Admin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.email'''

class Signup(models.Model):
     username = models.CharField(max_length = 100)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length = 100)
     confirm_password = models.CharField(max_length=100)
     isadmin = models.BooleanField(default=False)

def __str__(self):
     return self.username

class Login(models.Model):
     email = models.CharField(max_length=100)
     password = models.CharField(max_length = 100)

def __str__(self):
     return self.email

     

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


