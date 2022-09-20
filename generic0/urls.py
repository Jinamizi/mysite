from django.urls import path
from django.views.generic.dates import ArchiveIndexView, DateDetailView
from django.views.generic import DetailView

from . import views
from . import models

app_name='generic0'
urlpatterns = [
	path('publishers/', views.PublisherList.as_view()),
	path('books/<publisher>/', views.PublisherBookList.as_view()),
	path('contact/', views.ContactView.as_view(), name='contact'),

	path('authors', views.AuthorList.as_view(), name='author-list'),
	path('authors/add', views.AuthorCreate.as_view(), name='author-add'),
	path('authors/<int:pk>', views.AuthorDetail.as_view(), name='author-detail'),
	path('authors/<int:pk>/update', views.AuthorUpdate.as_view(), name='author-update'),
	path('authors/<int:pk>/delete', views.AuthorDelete.as_view(), name='author-delete'),

	path('archive/', ArchiveIndexView.as_view(model=models.Book, date_field='publication_date'), name="book-archive"),
	path('books/<int:pk>', DetailView.as_view(model=models.Book), name='book-details'),

	path('archive/<int:year>/', views.BookYearArchiveView.as_view(), name='book-year-archive'),
	#Example: archive/2012/08/
	path('archive/<int:year>/<int:month>/', views.BookMonthArchiveView.as_view(month_format='%m'), name='archive-month-numeric'),
	#Example: archive/2012/aug
	path('archive/<int:year>/<str:month>/', views.BookMonthArchiveView.as_view(), name='archive-month'),

	#Example: archive/2012/week/23
	path('archive/<int:year>/week/<int:week>/', views.BookWeekArchiveView.as_view(), name='archive-week'),

	#Example archive/2012/12/10
	path('archive/<int:year>/<int:month>/<int:day>/', views.BookDayArchiveView.as_view(month_format='%m'), name='archive-day-month-numeric'),
	#Example archive/2012/nov/10
	path('archive/<int:year>/<str:month>/<int:day>/', views.BookDayArchiveView.as_view(), name='archive-day'),
	
	path('archive/today/', views.BookTodayArchiveView.as_view(), name='archive-today'),

	path('archive/<int:year>/<int:month>/<int:day>/<int:pk>/', DateDetailView.as_view(model=models.Book, date_field='publication_date', month_format='%m'), name='archive-date-detail-month-numeric'),
	path('archive/<int:year>/<str:month>/<int:day>/<int:pk>/', DateDetailView.as_view(model=models.Book, date_field='publication_date'), name='archive-date-detail'),
]