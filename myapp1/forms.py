#contain our app form
from django import forms

from .models import Person

class LoginForm(forms.Form): 
	username = forms.CharField(max_length = 100)
	password = forms.CharField(widget = forms.PasswordInput())

	#making sure the user trying to login is present
	def clean(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		dbuser = Person.objects.filter(username=username, password=password)

		if not dbuser:
			raise forms.ValidationError("User does not exist in our db!")

		#return (username, password)
		