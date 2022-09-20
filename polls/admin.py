from django.contrib import admin

from .models import Question, Choice, Hint

class ChoiceInline(admin.TabularInline): #offers a tabular way of displaying inline related objects
	model = Choice
	extra = 3 #provide enough fields for 3 choices

class HintInline(admin.StackedInline):
	model = Hint
	extra = 1

class  QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text']
	#spliting the form into fieldsets
	fieldsets = [
		(None, {'fields': ['question_text']}), 
		('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline, HintInline] #Choices objects are edited on the Question admin page

	#To display individual fields
	list_display = ('question_text', 'pub_date', 'was_published_recently', 'total_votes_cast', 'total_comments', 'likes', 'dislikes')
	#add a "Filter" sidebar that lets people filter the change list by the pub_date field
	list_filter = ['pub_date']
	#add some search capabilities
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice) 