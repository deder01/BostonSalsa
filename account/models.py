# .. Imports

# Python
from __future__ import unicode_literals

# Django
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

# .. End Imports


# Account manager
class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')
        if not kwargs.get('first_name'):
            raise ValueError('Users must enter a valid first name.')

        account = self.model(
                email=self.normalize_email(email), **kwargs
        )

        account.set_password(password)
        account.save()

        return account
    
    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

# Account for a single user
class Account(AbstractBaseUser):
    # Validators
    # Store phone number in E.164 std format
    phone_regex = RegexValidator(regex=r'^\+?\d{9, 15}$', message="Phone number must be in +123456789 format, and between 9 and 15 digits.") 

    # Data
    # Basic Info
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50, blank=True)
    about_me = models.CharField(max_length = 200, blank=True)

    # Contact info
    email = models.EmailField(unique=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=16, validators=[phone_regex], blank=True)


    

    is_admin = models.BooleanField(default=False)

    # Meta data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=AccountManager()

    # lookup field and required fields (for superuser) 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
