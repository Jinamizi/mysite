from django.forms import ModelForm
from .models import Article
from django import forms


#Create the form class
class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['date_published', 'title', 'slug', 'content', 'is_draft', 'author']
