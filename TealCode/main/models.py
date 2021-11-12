from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length= 100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=200)
    code_text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    version = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    useful = models.IntegerField(default=0)
    not_useful = models.IntegerField(default=0)

    def __str__(self):
        return self.category.title + " - " + self.title
