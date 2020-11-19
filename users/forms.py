from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import ProfileInfo
from django import forms
from django.db import models


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields = ["image_user"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields = ["image_user"]
