from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    list = models.ForeignKey(List,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} --- {self.list}"

