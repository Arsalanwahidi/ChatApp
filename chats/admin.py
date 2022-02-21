from django.contrib import admin
from chats.models import GroupChat, GroupMessages

# Register your models here.

admin.site.register(GroupChat)
admin.site.register(GroupMessages)
