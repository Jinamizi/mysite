from django.urls import path

from . import views

app_name = 'examples'
urlpatterns = [
	path('register/', views.registerStudent, name = 'register'),
	path('<int:pk>/', views.StudentDisplay.as_view(), name='student_display'),
	path('example0/', views.example0, name='example0')
]