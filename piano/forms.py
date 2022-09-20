 from django import forms

 class SearchForm(forms.Form):
 	search_field = forms.CharField(label="CELL ", max_length=30)