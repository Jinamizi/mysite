from django.db import models
from django.conf import settings
from django.utils import timezone

class  Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	@property
	def full_name(self):
		return "%s %s" % (self.last_name, self.first_name)

	def __str__(self):
		return self.full_name
	
		
class Article(models.Model):
	title = models.CharField(max_length=70)
	slug = models.SlugField(max_length=70, unique=True)
	#author = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	date_published =models.DateTimeField(default=timezone.now)
	is_draft = models.BooleanField(default=True)
	content = models.TextField()

	def __str__(self):
		return self.title