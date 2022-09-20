from django.urls import path

from . import views

app_name = 'swahili'
urlpatterns = [
	path('corona/', views.corona, name='corona'),
	path('thika/', views.thika, name='thika'),
	path('serikalini/', views.serikalini, name='serikalini'),
]