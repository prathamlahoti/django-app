from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserSignupForm(UserCreationForm):
	""" Form to allow users sign up """

	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	""" Form to allow users update their info """

	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	""" Form to allow users update their profile info """

	class Meta:
		model = Profile
		fields = ['user_image']
