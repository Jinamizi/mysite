from django.urls import path

from . import views

app_name = 'bandcollections'
urlpatterns = [
	path('bands/', views.IndexView.as_view(), name='index'),
	path('register/', views.registerBand, name='register'),
	path('bands/<int:pk>/', views.BandView.as_view(), name='band'),
	path('bands/<int:band_id>/join', views.join, name='join'),
	path('register/<int:pk>/', views.RegisteredBand.as_view(), name='registration_successful'),
	path('bands/<int:band_id>/musicians/<int:musician_id>', views.musicianView, name='musician')
]