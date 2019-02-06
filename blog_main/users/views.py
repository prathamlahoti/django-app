from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserSignupForm


def signup(request):
	"""User Registration View"""
	if request.method == 'POST':
		signupForm = UserSignupForm(request.POST)
		if signupForm.is_valid():
			signupForm.save()
			messages.success(request, 'You were successfully signed up!')
			return redirect('login')
	else:
		signupForm = UserSignupForm()
	return render(request, "signup.html", {'form': signupForm})
