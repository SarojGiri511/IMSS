from typing import Any
from django.db import models


# Create your models here.
class inventory(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null = True)
    
    