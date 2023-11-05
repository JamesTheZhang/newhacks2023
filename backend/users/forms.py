from django import forms    
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import widgets

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(required=True)

    class Meta:
        model = User
        # All fields are required for user registration
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email'
        ]

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        labels = {
            'gender': 'Gender',
            'same_gender_pref': "Only find people of same gender as me",
            'fav_location': "Favourite Location on Campus",
            'major': "Major",
            'year_of_study': "Year of Study",
            'interests': "Interests",
            'profile_picture': "Profile Picture",
            "available": "I am currently available!"
        }
        fields = [
            'gender',
            'same_gender_pref',
            'fav_location',
            'major',
            'year_of_study',
            'interests',
            'profile_picture',
            'available'
        ]
