
from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ('username', 'email', 'password1', 'password2')

class CustomerProfileForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ('username', 'email')