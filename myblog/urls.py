from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>', views.DisplayView.as_view(), name='display'),
	path('compose/', views.save, name='compose'),
	#path('compose/', views.compose_article, name='compose'),
	path('save/', views.save, name='save')
]