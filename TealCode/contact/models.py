from django.db import models
from django.utils import timezone

class Entry(models.Model):
    ip = models.CharField(max_length=80)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=4000)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.email + " - " + self.subject


