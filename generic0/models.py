from django.db import models
from django.urls import reverse

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField(blank=True)
	class Meta:		
		def __str__(self):
			return self.name

class Author(models.Model):
	S = [
		('Mr', "Mr"),
		('Miss', "Miss"),
		('Mrs', "Mrs")
	]
	salutation = models.CharField(max_length=10, choices=S, blank=True)
	name = models.CharField(max_length=200)
	email = models.EmailField(blank=True)
	#headshot = models.ImageField(upload_to='author_headshots')

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('generic0:author-detail', kwargs={'pk':self.pk})

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publication_date = models.DateField()

	class Meta:
		ordering = ['title', '-publication_date', 'publisher']

	def get_absolute_url(self):
		return reverse('generic0:book-details', kwargs={'pk':self.pk})

	def __str__(self):
		return self.title

						