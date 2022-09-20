
from django.db import models, IntegrityError
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


'''
1. Stage names should be unique(in all cases)
'''

class Band(models.Model):
	stage_name = models.CharField(max_length=100, unique=True)
	date_formed = models.DateField(default=timezone.now)

	def add_musician(self, real_name, stage_name):
		self.musician_set.create(real_name=real_name, stage_name=stage_name)

	def is_viable(self):
		'''Check if a band has more than one musicians'''
		return self.number_of_musicians()	> 1 

	def  get_musicians(self):
		return self.musician_set.all()

	def number_of_musicians(self):
		return self.musician_set.count()

	def add_song(self, title, date_produced=timezone.now(), producer=None):
		self.music_set.create(title=title, date_produced=date_produced, producer=producer)

	def get_songs(self):
		return self.music_set.all()

	def number_of_songs(self):
		return self.music_set.count()

	def __str__(self):
		return self.stage_name

	@classmethod 
	def is_unique(cls,a_band):
		'''Tests if a given band is unique in all cases'''
		return Band.objects.filter(stage_name__iexact=a_band).count() != 0 

	def clean(self):
		if Band.objects.filter(stage_name__iexact=self.stage_name).count() != 0:
			raise ValidationError({'stage_name':_('Stage name has already been taken')})

	'''
	def save(self, *args, **kwargs):
		if Band.objects.filter(stage_name__iexact=self.stage_name).count() != 0:
			raise IntegrityError('UNIQUE constraint failed: bandcollections_band.stage_name')
		super().save(*args, **kwargs)
	'''

class Musician(models.Model):
	real_name = models.CharField(max_length=100, null=True)
	stage_name = models.CharField(max_length=100, unique=True)
	band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.stage_name

	def get_band(self):
		return self.band

	get_band.admin_order_field = 'Band'

	def clean(self):
		if Band.objects.filter(stage_name__iexact=self.stage_name).count() != 0:
			raise ValidationError({'stage_name':_('Stage name has already been taken')})

	def save(self, *args, **kwargs):
		if Musician.objects.filter(stage_name__iexact=self.stage_name).count() != 0:
			raise IntegrityError('UNIQUE constraint failed: bandcollections_musician.stage_name')
		super().save(*args, **kwargs)

class  Music(models.Model):
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	date_produced = models.DateField()
	producer = models.CharField(max_length=100)

	def get_band(self):
		return self.band

	def __str__(self):
		return self.title

'''
DI = Descriptive information: used to describe something
	eg: Migos- A band that has three members.
TI = Tabular Information: Used to form tabular data
	eg Date of Birth  - 20/12/1997
'''
class MusicianDI(models.Model):
	"""description of a Musician"""
	musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	information = models.TextField(blank = False)
	
	def __str__(self):
		return self.title

class MusicianTI(models.Model):
	"""description of a Musician"""
	musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	information = models.CharField(max_length=100, blank = False)
	
	def __str__(self):
		return self.title

class BandDI(models.Model):
	"""description of a Band"""
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	information = models.TextField(max_length=100, blank = False)
	
	def __str__(self):
		return self.title

class BandTI(models.Model):
	"""Information of a Band"""
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	information = models.CharField(max_length=100, blank = False)
	
	def __str__(self):
		return self.title

class MusicTI(models.Model):
	"""description of a Music"""
	music = models.ForeignKey(Music, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	information = models.CharField(max_length=100, blank = False)
	
	def __str__(self):
		return self.title

class MusicDI(models.Model):
	"""description of a Music"""
	music = models.ForeignKey(Music, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	information = models.TextField(max_length=100, blank = False)
	
	def __str__(self):
		return self.title