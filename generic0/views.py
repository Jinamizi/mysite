from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormView
from django.views.generic.dates import YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, TodayArchiveView

from .forms import ContactForm
from .models import *

class PublisherList(ListView):
	model = Publisher
	
"""
If we wanted to write a view that displayed all the books by some arbitrary publisher?
override get_queryset()
when class-based views are called, various useful things are stored on self: 
as well as the request(self.request) this includes the positional(self.args) and name-based(self.kwargs)
 arguments captured according to the URLconf.
"""
class PublisherBookList(ListView):
	template_name = 'generic0/books_by_publisher.html'

	def get_queryset(self):
		self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
		return Book.objects.filter(publisher=self.publisher)

	#We can also add the context at the same time, so we can use it in the template:
	def get_context_data(self, **kwargs):
		#call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		#Add in the publisher
		context['publisher'] = self.publisher
		return context

"""
Form processing generally has 3 paths:
-Initial GET(blank or prepopulated form)
-POST with invalid data(typically redisplay form with errors)
-POST with valid data(process the data and typically redirect)
"""

class ContactView(FormView):
	template_name = "generic0/contact.html"
	form_class = ContactForm
	success_url = 'generic0/thanks.html'

	def form_valid(self, form):
		#This method is called when valid form data has been POSTed.
		#It should return an HttpResponse
		form.send_email()
		return super().form_valid(form)
"""
Notes:
-FormView inherits TemplateResponseMixin so template_name can be used here.
-The default implementation for form_valid() simply redirects to the success_url
"""
'''
In the example below
The views inherit SingleObjectTemplateResponseMixin whic uses template_name_suffix to construct the template_name 
based on the model.
-CreateView and UpdateView use generic0/author_form.html
-DeleteView uses generic0/author_confirm_delete.html
If you wish to have separate templates for CreateView and UpdateView, you can set either template_name or 
template_name_suffix on your view class.
'''
class AuthorCreate(CreateView):
	model = Author
	fields = ['salutation', 'name', 'email']

class AuthorUpdate(UpdateView):
	model = Author
	fields = ['salutation', 'name', 'email']

class AuthorDelete(DeleteView):
	model = Author
	success_url = reverse_lazy('generic0:author-list') 
	#we use reverse_lazy() instead of reverse, as the urls are not loaded when the file is imported

class AuthorDetail(DetailView):
	model = Author
	template_name = 'generic0/author.html'

class AuthorList(ListView):
	model = Author
	context_object_name = 'authors'
	template_name = 'generic0/authors_list.html'

class BookYearArchiveView(YearArchiveView):
	queryset = Book.objects.all()
	date_field = 'publication_date'
	make_object_list = True
	allow_future = True

class BookMonthArchiveView(MonthArchiveView):
	queryset = Book.objects.all()
	date_field = 'publication_date'
	allow_future = True
	allow_empty = True

class BookWeekArchiveView(WeekArchiveView):
	queryset = Book.objects.all()
	date_field = 'publication_date'
	week_format = '%W' #week begins on Monday. %U week begins on Sunday
	allow_future = True
	#allow_empty = True

class BookDayArchiveView(DayArchiveView):
	queryset = Book.objects.all()
	date_field = 'publication_date'
	allow_future = True
	allow_empty = True

'''
This view uses by default the same template as the DayArchiveView. If you need a
different template, set the template_name attribute to be the name of the new template
'''
class BookTodayArchiveView(TodayArchiveView):
	queryset = Book.objects.all()
	date_field = 'publication_date'
	allow_future = True
	allow_empty = True



