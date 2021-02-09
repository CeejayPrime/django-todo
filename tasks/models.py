from django.db import models
from django.db.models import CharField


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SubTask(models.Model):
    Subtitle = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Subtitle


