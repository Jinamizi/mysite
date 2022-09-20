from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'myapp1'
'''urlpatterns = [
	# ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]'''
urlpatterns = [
 	#path('connection/', TemplateView.as_view(template_name = 'myapp1/login.html')),
 	path('connection/', views.display, name='display'),
 	path('login/', views.login, name='login')
 ]