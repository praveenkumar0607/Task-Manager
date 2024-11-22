from django.db import models
from django.contrib.auth.models import User
class task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title_task = models.CharField(max_length=100)
    description_task = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title_task
