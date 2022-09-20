from django.test import TestCase
from django.utils import timezone
from .models import *

class MusicianModelTest(TestCase):
	pass

class BandModelTest(TestCase):
	def test_add_musician(self):
		band = Band(stage_name="stage_name", date_formed=timezone.now())
		band.add_musician(real_name='real_name', stage_name='stage_name')
		self.assertTrue(band.musician_set.count() > 0)

	def test_is_viable(self):
		band = Band.objects.create(stage_name="stage_name", date_formed=timezone.now())
		self.assertFalse(band.is_viable())
		'''
		band.add_musician(real_name='real_name', stage_name='stage_name')
		self.assertFalse(band.is_viable())
		band.add_musician(real_name='real_name', stage_name='stage_name')
		self.assertTrue(band.is_viable())'''