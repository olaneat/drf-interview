from django.db import models

# Create your models here.
class TaskModel(models.Model):
    name = models.CharField(max_length=255, ) #task name field is created in the DB
    completed = models.BooleanField(default=False) # completed field is created in the DB
    created_at = models.DateTimeField(auto_now_add=True) #created_at field is created in the DB


    class Meta: # a class used to query the db is created
        ordering = ('-created_at',) #DB is queried in ascending order