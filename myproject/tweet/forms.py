from django import forms 
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
     class Meta:
        model = Tweet
        fields = ['text', 'photo']    # made by us that's why aaray


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()        
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')                  # built using Django therefore tuple