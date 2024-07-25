from django.db import models
from django.utils import timezone
class User(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name

class Message(models.Model):
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField(max_length=500)
    author = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30, blank=False, default="ToGod")

    def __str__(self):
        return self.text
