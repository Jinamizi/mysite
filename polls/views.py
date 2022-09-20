from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice, QuestionComment, CommentComment 

'''ListView and DetailView abstract the concept of "display a list of objects" and "display a detail page for a particular type of object".'''

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	model = Question


	def get_queryset(self):
		"""Excludes any questions that arent published yet."""
		return Question.objects.filter(pub_date__lte=timezone.now())

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
	
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'	

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form.
		return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select a choice"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def comments_on_comment(request, comment_id):
	"""Display comments of a comment with a given comment_id."""
	comment = get_object_or_404(QuestionComment, pk=comment_id)
	comments_on_comment = comment.commentcomment_set.all() #get all commets for a given comment
	paginator = Paginator(comments_on_comment, 10) #show 10 comments per view

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'polls/comments_on_comment.html', {'comment':comment, 'page_obj': page_obj})

def add_comment(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	if request.method == 'POST':
		question.questioncomment_set.create(comment_text=request.POST['comment'], date_commented=timezone.now())

	return HttpResponseRedirect(reverse('polls:question_comments', args=(question.id,)))

def add_comment_on_comment(request, comment_id):
	comment = get_object_or_404(QuestionComment, pk=comment_id)

	if request.method == 'POST':
		comment.commentcomment_set.create(comment_text=request.POST['comment'], date_commented=timezone.now())

	return HttpResponseRedirect(reverse('polls:comments_on_comment', args=(comment.id, )))

def like_question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	question.likes += 1
	question.save()

	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def dislike_question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	question.dislikes += 1
	question.save()

	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def like_comment(request, comment_id):
	comment = get_object_or_404(QuestionComment, pk=comment_id)
	comment.likes += 1
	comment.save()

	return HttpResponseRedirect(reverse('polls:question_comments', args=(comment.question.id,)))

def dislike_comment(request, comment_id):
	comment = get_object_or_404(QuestionComment, pk=comment_id)
	comment.dislikes += 1
	comment.save()

	return HttpResponseRedirect(reverse('polls:question_comments', args=(comment.question.id,)))

def like_comment_on_comment(request, commentcomment_id):
	comment = get_object_or_404(CommentComment, pk=commentcomment_id)
	comment.likes += 1
	comment.save()

	return HttpResponseRedirect(reverse('polls:comments_on_comment', args=(comment.comment.id,)))

def dislike_comment_on_comment(request, commentcomment_id):
	comment = get_object_or_404(CommentComment, pk=commentcomment_id)
	comment.dislikes += 1
	comment.save()

	return HttpResponseRedirect(reverse('polls:comments_on_comment', args=(comment.comment.id,)))

#Learning
class CommentList(generic.ListView):
	paginate_by = 2 #helps to paginate the displayed list. This limits the number of objects per page and adds a paginator and page_obj to the context
	model = QuestionComment

class QuestionList(generic.ListView):
	paginate_by = 5
	model = Question
	template_name = "polls/questions_display.html"

#using paginator in a view function
from django.core.paginator import Paginator 

def question_comments(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	comments = question.questioncomment_set.all()
	paginator = Paginator(comments, 10) #show 10 comments per view

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'polls/question_comments.html', {'question':question, 'page_obj': page_obj})

def login(request):
	pass