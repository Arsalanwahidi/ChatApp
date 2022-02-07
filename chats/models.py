from django.db import models

# Create your models here.

# class Room(models.Model):
#     name = models.CharField(max_length=50)

# class User(models.Model):
#     username = models.CharField(max_length=250)
#     password = models.CharField(max_length=250)
#     email = models.EmailField(max_length=250)

class GroupChat(models.Model):
    group = models.CharField(max_length=500)
