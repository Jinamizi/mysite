from django.urls import path

from . import views

app_name = "comments"
urlpatterns = [
	path('', views.login, name='login'),
	path('index/', views.IndexView.as_view(), name='index'),
	path('signin/', views.signin, name='signin')
]