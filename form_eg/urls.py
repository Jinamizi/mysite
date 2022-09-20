from django.urls import path
from django.views.generic import TemplateView

from . import views

appname = 'form_eg'
urlpatterns = [
	path('name/', views.get_name, name='name'),
	path('contact/', views.contact, name='contact'),
	path('contact1/', TemplateView.as_view(template_name='form_eg/contact1.html'))
]