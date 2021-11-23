from django.db import models
from django.utils import timezone
from main.models import Topic, Category



class View(models.Model):
    ip = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    country = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    custom_title = models.CharField(max_length=250, blank=True)



    def __str__(self):
        a = self.ip
        
        if self.country:
            a = a + " - " + self.country
        
        if self.topic:
            a = a + " - " + self.topic.title

        if self.category:
            a = a + " - " + self.category.title

        if self.custom_title:
            a = a + " - " + self.custom_title

        a = a + " - " + str(self.date.day) + "." + str(self.date.month) + "." + str(self.date.year)
        return a
