from django import forms

class UserInfoForm(forms.Form):
    first_name = forms.CharField(max_length=250)