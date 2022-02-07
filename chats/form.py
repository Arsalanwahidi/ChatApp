from attr import fields
from django import forms
from chats.models import GroupChat

class GroupData(forms.ModelForm):

    class Meta:
        model = GroupChat
        fields = ['group']