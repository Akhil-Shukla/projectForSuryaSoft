# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from decimal import Decimal

# Create your models here.
class User(models.Model):
    name=models.CharField(default="aaaa",max_length=50)
    valid = models.BooleanField(default=True)


class Expense(models.Model):
    client_id=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(default=None,max_length=100)
    timestamp=models.DateTimeField(auto_now=True)
    amount=models.IntegerField(default=10)
    description=models.CharField(default="aaaa",max_length=100)
