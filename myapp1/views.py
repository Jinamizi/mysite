from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from myapp1.forms import LoginForm
from .models import Person

#this view will display the result of the login form posted through the logged.html
def login(request):
	username = 'not logged in'

	if  request.method == 'POST':
		#Get the posted form
		MyLoginform = LoginForm(request.POST)

		if MyLoginform.is_valid():
			username = MyLoginform.cleaned_data['username']
			return render(request, 'myapp1/loggedin.html', {"username":username})
	else:
		MyLoginform = LoginForm()

	return render(request, 'myapp1/login1.html', {"form":MyLoginform})
	#return HttpResponse("You are: %s" % username)

def display(request):
	form = LoginForm()
	return render(request, 'myapp1/login1.html', {"form" : form})