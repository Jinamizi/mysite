from django.db import models
from django.utils import timezone
from django.urls import reverse

class User(models.Model):
	username = models.CharField(max_length=150, unique=True)
	password = models.CharField(max_length=150)
	email = models.EmailField(max_length=150, blank=True)
	date_joined = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ["username"]

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse('actilist:user-profile', kwargs={'pk':self.pk})

	def activity_count(self):
		return self.activity_set.count()
	activity_count.short_description = 'activities'

	def activity_completed_count(self):
		return self.activity_set.filter(done=True).count()

	def activity_uncompleted_count(self):
		return self.activity_set.filter(done=False).count()

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	activity_description = models.TextField()
	start_time = models.DateTimeField()
	done_time = models.DateTimeField()
	done = models.BooleanField(default=False)
	date_added = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ["-date_added", "-start_time", "activity_description"]
		verbose_name_plural = 'activities'