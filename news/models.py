from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Reporter(models.Model):
	first_name = models.CharField(max_length=70, default=None, null=True)
	last_name = models.CharField(max_length=70, default=None, null=True)
	sirname = models.CharField(max_length=70, default=None, null=True)

	def clean(self):
		if len(self.first_name.split(' ')) != 0 or len(self.last_name.split(' ')) != 0 or len(self.sirname.split(' ')) != 0:
			raise ValidationError(_('Names should not have spaces between them.'))
		
	def __str__(self):
		return "%s %s %s" % (self.last_name, self.first_name, self.sirname)

class Article(models.Model):
	pub_date = models.DateField()	
	headline = models.CharField(max_length=200)
	content = models.TextField()
	reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

	def __str__(self):
		return self.headline