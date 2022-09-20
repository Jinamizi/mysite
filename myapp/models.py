from django.db import models

class Singer(models.Model):
	stage_name = models.CharField(max_length=100)

	class Meta:
		abstract = True

class Band(Singer):
	date_formed = models.DateField()

class Musician(Singer):
	real_name = models.CharField(max_length=100)

	def __str__(self):
		return Singer.stage_name

class DescriptiveInfo(models.Model):
	singer = models.ForeignKey(Singer, on_delete=models.CASCADE)	
	title = models.CharField(max_length=100)
	info = models.TextField()	

class TabularInfo(models.Model):
	singer = models.ForeignKey(Singer, on_delete=models.CASCADE)	
	title = models.CharField(max_length=100)
	info = models.CharField(max_length=100)
		