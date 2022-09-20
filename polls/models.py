import datetime

from django.db import models
from django.utils import timezone

class Member(models.Model):
	username = models.CharField(max_length=150)
	password = models.CharField(max_length=150)
	email = models.CharField(max_length=150)
	date_joined = models.DateTimeField('date joined')

	class Meta:
		ordering = ["-date_joined", "username"]

	def __str__(self):
		return self.username

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)

	class Meta:
		ordering = ['-pub_date']
			

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	#to improve the name of the method in the admin page
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	def total_votes_cast(self):
		"""returns the total votes cast on this question"""
		return sum([choice.votes for choice in self.choice_set.all()])
	total_votes_cast.short_description = "Total votes";

	def total_comments(self):
		"""returns the sum of all comments posted on this question."""
		total = sum([comment.commentcomment_set.count() for comment in self.questioncomment_set.all()]) #get sum of comment on comments
		return self.questioncomment_set.count() + total
	total_comments.short_description = "Total comments";


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	class Meta:
		ordering = ['-votes']
			

	def __str__(self):
		return self.choice_text

	def get_percentage(self):
		"""gets the percentage of votes this choice got"""
		return round((self.votes / self.question.total_votes_cast()) * 100, 1)


class Hint(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	hint_text = models.TextField(max_length=200)

	def __str__(self):
		return self.hint_text

class AbstractComment(models.Model):
	comment_text = models.TextField(max_length=400, default="")
	date_commented = models.DateTimeField()
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)

	class Meta:
		abstract = True
		ordering = ['-date_commented', 'likes']

	def __str__(self):
		return self.comment_text
		

class QuestionComment(AbstractComment):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	
class CommentComment(AbstractComment):
	comment = models.ForeignKey(QuestionComment, on_delete=models.CASCADE)