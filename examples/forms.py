from django import forms

from examples.models import Student, Person, Example0
from . import validators

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student	
		fields = ['name', 'age', 'home_group', 'year_in_school']

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person	
		fields = '__all__'

class  Example0Form(forms.ModelForm):
	'''even_field = forms.IntegerField(validators=[validators.validate_even])'''
	class Meta:
		model = Example0
		fields = ['even_field']