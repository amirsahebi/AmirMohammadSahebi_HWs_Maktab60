from os import major
from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    lessons = models.ManyToManyField("environment.Lesson")

class Student(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    major = models.CharField(max_length=255)
    lessons = models.ManyToManyField("environment.Lesson")