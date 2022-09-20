from django import forms
from django.core.exceptions import ValidationError

def validate_length(value):
	if len(value)% 2 == 0:
		raise ValidationError(
			_('%(value)s is unacceptable length'), 
			params={'value': len(value) }
		)

'''class  LengthValidatedField(forms.CharField):
	default_validators = [validate_length]	'''

class NameForm(forms.Form):
	your_name = forms.CharField(label="You name", max_length=100, validators=[validate_length])

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100, help_text="Type the subject of your message here.")
	message = forms.CharField(widget=forms.Textarea, help_text = "Type your message here.")
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

