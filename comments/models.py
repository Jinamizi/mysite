from django.db import models

class User(models.Model):
	username = models.CharField(max_length = 40, unique = True)
	password = models.CharField(max_length = 40)
	email = models.EmailField()
	date_joined = models.DateField()

	def __str__(self):
		return self.username

	def text_count(self):
		return self.text_set.count()

class Text(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateField()

class Comment(models.Model):
	text = models.ForeignKey(Text, on_delete=models.CASCADE)
	comment = models.TextField()
	date = models.DateField()
		

		