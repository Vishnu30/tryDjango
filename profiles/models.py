from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class profile(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField(default='description default text')

    def __str__(self):
        return self.name
