from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.hashers import make_password, check_password

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)  # Store hashed passwords in a real app
    department = models.CharField(max_length=100, null=True, blank=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class Request(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')

# class Controller(AbstractBaseUser):
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=255, unique=True,null=True,blank=True)
#     role = models.CharField(max_length=50,null=True,blank=True)
#     password = models.CharField(max_length=100,null=True,blank=True)  # For compatibility with AbstractBaseUser

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'role']

#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
    
#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)


class ControllerManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class Controller(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True,null=True)
    role = models.CharField(max_length=50,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = ControllerManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
