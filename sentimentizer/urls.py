from django.urls import path
from . import views

app_name = 'sentimentizer'
urlpatterns = [
 	path('', views.analyze, name='analyze'),
 ]