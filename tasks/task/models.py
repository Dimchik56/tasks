from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    titletask = models.CharField(max_length=100)
    texttask = models.TextField(blank=True)
    datecreatedtask = models.DateTimeField(auto_now_add=True)
    datecompletedtask = models.DateTimeField(null=True, blank=True)
    importanttask = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titletask