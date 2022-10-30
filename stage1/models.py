from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Stage1(models.Model):
    slackUsername = models.CharField(max_length = 50)
    backend = models.BooleanField(default = False )
    age = models.IntegerField()
    bio = models.CharField(max_length  = 50)
# Create your models here.
