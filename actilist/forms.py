from django import forms
from django.core.exceptions import ValidationError

from . import models

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	def is_valid(self):
		super().is_valid()
		if (models.User.objects.filter(username=self.cleaned_data['username'])):
			user = models.User.objects.get(username=self.cleaned_data['username'])
			if user.password == self.cleaned_data['password']:
				return True
			else:
				self.error["password-error"] = ["The password you entered is incorrect"]
		else:
			self.error["username-error"] = ["Username do not exist."]

		return False

class CreateAccountForm(forms.ModelForm):
	"""A form for creating new users."""
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
	password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput())

	class Meta:
		model = models.User
		fields = ['username', 'email']

	def clean_password2(self):
		#check that the two password entries match
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 and password2:
			raise ValidationError("Passwords don't match")
		return password2

	def is_valid(self):
		super().is_valid()
		'''if self.cleaned_data['password'] != self.cleaned_data[confirm_password]:
			self.error['password-error'] = ['passwords need to be the same']'''
		if (models.User.objects.filter(username=self.cleaned_data['username'])):
			self.error["username-error"] = ['Username exist']
			return False
		return True

	def save(self, commit=True):
		user = super().save(commit=False)
		user.password = self.cleaned_data['password']
		if commit:
			user.save()
		return user