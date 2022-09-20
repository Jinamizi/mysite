from django import forms
from django.core.exceptions import ValidationError

from bandcollections.models import Band, Musician

class BandForm(forms.ModelForm):
	'''	Used to register a band'''
	class Meta:
		model = Band
		fields = ['stage_name']

class JoinForm(forms.ModelForm):
	'''	Used to join a band	'''
	class Meta:
		model = Musician	
		fields = ['stage_name', 'real_name']