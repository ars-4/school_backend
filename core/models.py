from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class Type(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SClass(BaseModel):
    title = models.CharField(max_length=255, default='None')

    def __str__(self):
        return self.title


class Subject(BaseModel):
    title = models.CharField(max_length=255, default='None')

    def __str__(self):
        return self.title


class Person(BaseModel):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    s_classes = models.ManyToManyField(SClass)
    subjects = models.ManyToManyField(Subject)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.roll_no

