from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.views.generic.list import ListView

from .models import Article

def year_archive(request, year):
	a_list = Article.objects.filter(pub_date__year = year)
	context = {'year': year, 'article_list': a_list}
	return render(request, 'news/year_archive.html', context)

def month_archive(request, year:int, month:int):
	pass

def article_detail(request, year, month, pk):
	pass

class ArticlesView(generic.ListView):
	template_name = 'news/index.html'
	context_object_name = 'articles'

	def get_queryset(self):
		return Article.objects.all()

class DetailView(generic.DetailView):
	model = Article
	template_name = 'news/detail.html'

class ArticleListView(ListView):
	model = Article
	paginate_by = 100 # if pagination is desired

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
