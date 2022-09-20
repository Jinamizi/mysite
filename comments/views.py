from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import models
from . import forms

class  IndexView(generic.ListView):
	template_name = 'comments/index.html'
	model = models.Text

def signin(request):
	"""Sign in a user"""
	if request.method == 'POST':
		form = forms.SignInForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			user.date_joined = timezone.now()
			user.save()
			return HttpResponseDirect(reverse('comments:index'))
	else:
		form = forms.SignInForm()
	return render(request, 'comments/signin.html', {'form': form})

def login(request):
	"""Log in a user"""
	if request.method == 'POST':
		form = forms.LoginForm(request.POST)

		if form.is_valid():
			
			
			return HttpResponseDirect(reverse('comments:index'))
	else:
		form = forms.LoginForm()
	return render(request, 'comments/login.html', {'form': form})
		
		
