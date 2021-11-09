from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    

class CollegeLesson(models.Model):
    college = models.CharField(max_length=255)
    lesson = models.ForeignKey("environment.Lesson",on_delete=models.CASCADE)

    class Meta:
        unique_together = ['college','lesson']


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    classes = models.ManyToManyField("environment.Classes")


class Classes(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
