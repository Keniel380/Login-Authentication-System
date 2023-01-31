from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class loginapp(models.Model):
   First_name = models.fields.CharField(max_length=50)
   Last_name = models.fields.CharField(max_length=50)
   Gender = models.fields.CharField(max_length=5, blank= True, null=True)
   Email = models.fields.CharField(max_length=50)
   Password = models.fields.CharField(max_length=50)
   Re_password = models.fields.CharField(max_length=50)

