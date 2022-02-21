from attr import fields
from django import forms
from chats.models import GroupChat, GroupMessages

class GroupData(forms.ModelForm):

    class Meta:
        model = GroupChat
        fields = ['group']

class GroupMessagesForm(forms.ModelForm):

    class Meta:
        model = GroupMessages
        fields = ['messages']