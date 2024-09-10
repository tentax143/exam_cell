from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords in a real app
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Request(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')
