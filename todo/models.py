from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class ToDoList(models.Model):
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    content     = models.TextField(max_length=1000)
    completed   = models.BooleanField(default=False)
    created_at  = models.DateTimeField(default=now)
    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.author} | {self.content[0:19]}..."