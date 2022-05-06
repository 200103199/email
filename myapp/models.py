
from pydoc import describe
from django.db import models



class Emp(models.Model):

    name = models.TextField(max_length=255,verbose_name="name", )
    age = models.IntegerField(verbose_name="age")


