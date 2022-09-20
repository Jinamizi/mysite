from django import forms
from django.core.exceptions import ValidationError

from comments import models

class SignInForm(forms.ModelForm):
	"""Used to sign in a user"""
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	confirm_password = forms.CharField(label="Confirm password", widget=forms.PasswordInput())

	class Meta:
		model = models.User
		fields = ['username', 'email']

	def clean_password(self):
		"""Check that the two password entries match"""
		password1 = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("confirm_password")

		if password1 and password2 and password1 != password2:
			raise ValidationError("Passwords don't match")

		return password2

	def save(self, commit=True):
		"""Save the provided password in hashed format"""
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user

class LoginForm(forms.ModelForm):
	class Meta:
		model = models.User
		fields = ['username', 'password']

	#making sure the user trying to login is present
	def clean(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		dbuser = User.objects.filter(username=username, password=password)

		if not dbuser:
			raise forms.ValidationError("User does not exist in our db!")

			
		