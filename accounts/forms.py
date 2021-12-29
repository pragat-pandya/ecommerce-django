from django import forms
from .models import Account

class RegistrationForm (forms.Model):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
