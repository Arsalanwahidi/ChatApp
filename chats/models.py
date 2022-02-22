from django.db import models
from datetime import datetime
from django.utils import timezone

class GroupChat(models.Model):
    group = models.CharField(max_length=500, null=True, blank=True)

class GroupMessages(models.Model):
    messages = models.CharField(max_length=100000, null=True, blank=True)
    user = models.CharField(max_length=255, null=True)
    date = models.DateField(timezone.now().time())
