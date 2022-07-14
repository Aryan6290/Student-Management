from decimal import Decimal
from django.db import models
from django.forms import DecimalField

# Create your models here.


class Student(models.Model):
    name = models.CharField(null=False, blank = False,max_length=200)
    grade = models.IntegerField(null=False, blank = False)
    section = models.CharField(null=False, blank = False,max_length=1)
    roll = models.IntegerField(null=False, blank = False)

    def __str__(self):
        return self.name

