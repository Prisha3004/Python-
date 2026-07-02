from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField()
    email=models.EmailField()
    enrollment=models.IntegerField(unique=True,default=None)
    contact=models.IntegerField(default=None)
