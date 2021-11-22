from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from taggit.managers import TaggableManager

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length= 100)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=200)
    code_text = models.TextField()
    output = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    version = models.CharField(max_length=100, blank=True)
    read_more = models.TextField(blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.category.title + " - " + self.title

class Rating(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    is_positive = models.BooleanField()
    ip = models.CharField(max_length=90 )
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic.title + " - " + self.ip