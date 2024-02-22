from typing import Any
from django.db import models


# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    added= models.DateField(null=True)
    upadte=models.DateField(null=True)