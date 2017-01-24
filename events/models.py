from __future__ import unicode_literals

from django.db import models
from address.models import AddressField

# A dance event
class Event(models.Model):
    address = AddressField()
