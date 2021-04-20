from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserregisterionForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['password1'].help_text = ' '
        self.fields['password2'].help_text = ' '
        self.fields['username'].help_text = ' '