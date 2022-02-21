from cProfile import label
from django.db import models

class GroupChat(models.Model):
    group = models.CharField(max_length=500, null=True, blank=True)

class GroupMessages(models.Model):
    messages = models.CharField(max_length=100000, null=True, blank=True)
