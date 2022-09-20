from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

app_name = 'news'
urlpatterns = [
	path('', views.ArticleListView.as_view(), name='article-list'),
	path('article', views.ArticlesView.as_view(), name='index'),
	path('article/<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('article/<yyyy:year>/', views.year_archive),
	path('article/<yyyy:year>/<int:month>/', views.month_archive),
	path('article/<yyyy:year>/<int:month>/<int:pk>/', views.article_detail),
]