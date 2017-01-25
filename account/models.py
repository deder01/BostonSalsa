from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.base_user.models import AbstractBaseUser

# Account for a single user
class Account(AbstractBaseUser):
    # Basic Info
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    about_me = models.CharField(max_length = 200, blank=True)

    # Contact info
    email = Models.EmailField(unique=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], blank=True)

    # Validators

    # Store phone number in E.164 std format
    phone_regex = RegexValidator(regex=r'^\+?\d{9, 15}$', message="Phone number must be in +123456789 format, and between 9 and 15 digits.") 

    

    is_admin = models.BooleanField(default=False)

    # Meta data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=AccountManager()

    # lookup field and required fields
    REQUIRED_FIELDS = ['email', 'first_name']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
