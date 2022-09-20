from django.urls import path
from django.views.generic import DetailView

from . import views, models

app_name = 'actilist'
urlpatterns = [
	path('', views.LoginView.as_view(), name='index'),
	path('login/', views.LoginView.as_view(), name='login'),
	path('signup/', views.CreateAccountView.as_view(), name='signup'),
	path('<int:pk>/profile', DetailView.as_view(model=models.User), name='user-profile'), #one should pass username instead of pk
	path('actilist/<str:username>/activities', views.UserActivitiesList.as_view(), name='user-activities'),
]