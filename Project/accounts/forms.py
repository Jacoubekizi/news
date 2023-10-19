from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="confirmation Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CustomUser
        fields = ['email', 'username',]