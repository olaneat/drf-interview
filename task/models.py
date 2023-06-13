from django.db import models

# Create your models here.
class TaskModel(models.Model):
    name = models.CharField(max_length=255, )
    completed = models.BooleanField(default=False)
