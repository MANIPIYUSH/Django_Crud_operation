
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Emp(models.Model):
    emp_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    dob=models.CharField(max_length=50)
    doj=models.CharField(max_length=50)
    department=models.CharField(max_length=200)
    post=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    zip_code=models.CharField(max_length=10)
    state=models.CharField(max_length=50)
    onleave=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name