from django.db import models

from django.utils import timezone
from main.models import Topic, Category

class View(models.Model):
    ip = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    admin = models.BooleanField(default=False)
    home = models.BooleanField(default=False)



    def __str__(self):
        return self.ip
