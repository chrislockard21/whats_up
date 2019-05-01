from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoItem(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.content
