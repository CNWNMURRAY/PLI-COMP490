from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.



'''class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title'''


class Course(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE, default='None')
    #subject = models.ForeignKey(Subject,  on_delete=models.CASCADE, default='None' )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE) #changed
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title