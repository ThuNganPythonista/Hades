from django import forms
import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='password', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
        raise forms.ValidationError("There is something wrong !")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+&', username):
            raise forms.ValidationError("The account name contains special characters")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Account existed!")