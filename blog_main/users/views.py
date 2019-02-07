from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm


def signup(request):
	"""User Registration View"""
	if request.method == 'POST':
		signup_form = UserSignupForm(request.POST)
		if signup_form.is_valid():
			signup_form.save()
			messages.success(request, 'You were successfully signed up!')
			return redirect('login')
	else:
		signup_form = UserSignupForm()
	return render(request, "signup.html", {'form': signup_form})


@login_required
def profile(request):
	""" User profile view """
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Your profile has been updated')
			return redirect('profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

	return render(request, 'profile.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})
