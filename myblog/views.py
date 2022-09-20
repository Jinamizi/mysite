from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect

from .models import Article, Author
from myblog.forms import ArticleForm

def compose_article(request):
	form = ArticleForm()
	return render(request, 'myblog/get_article.html', {'form':form})

def save(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST) #Create a form instance from POST data.

		if form.is_valid():
			#Save a new Article objects from the form's data.
			new_article = form.save()
			#return an HttpResponseRedirect after successfully dealing with POST data. This prevent data from being posted twice if a user hits the Back button
			return render(request, 'myblog/display.html', {'article':new_article}) 
	else:
		form = ArticleForm()

	return render(request, 'myblog/get_article.html', {'form':form})

class DisplayView(generic.DetailView):
	model = Article
	template_name = 'myblog/display.html'

class IndexView(generic.ListView):
	model = Article
	template_name = 'myblog/index.html'
	context_object_name = 'articles'
	