from django.db import models

# Create your models here.
class City(models.Model):
	"""docstring for City"""
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Shop(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)	

	def __str__(self):
		return self.name + "_" + self.city	