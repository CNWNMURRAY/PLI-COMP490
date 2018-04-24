from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='Unknown')
    #subject = models.ForeignKey(Subject,  on_delete=models.CASCADE, default='None' )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='None')
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

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200, default='Unknown')
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.CharField(max_length=200)
    number_of_responses = models.IntegerField(default=0)
    
    def __str__(self):
        return self.response_text

class Content(models.Model):
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, limit_choices_to={'model__in':('text','video','image','file')}, on_delete=models.CASCADE) 
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')    


class ItemBase(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()
    file = models.FileField(upload_to='video', default='None')