from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from main.models import Category,Topic

class View(models.Model):
    ip = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=CASCADE)
    category = models.ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.ip
