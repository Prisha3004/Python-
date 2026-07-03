from django.db import models

# Create your models here.

class Course(models.Model):
    name=models.CharField()
    code=models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.code})"
    

class Student(models.Model):
    name=models.CharField()
    email=models.EmailField()
    enrollment=models.IntegerField(unique=True,default=None)
    contact=models.IntegerField(default=None)
    courses=models.ManyToManyField(Course)