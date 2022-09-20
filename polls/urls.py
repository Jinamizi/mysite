from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
 	path('', views.QuestionList.as_view(), name='index'),
 	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
 	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
 	path('<int:question_id>/vote/', views.vote, name='vote'),
 	path('<int:question_id>/addcomment', views.add_comment, name='add_comment'),
 	path('<int:question_id>/like', views.like_question, name='like_question'),
 	path('<int:question_id>/dislike', views.dislike_question, name='dislike_question'),
 	path('comment/<int:comment_id>/addcomment', views.add_comment_on_comment, name='add_comment_on_comment'),
 	path('comment/<int:comment_id>/like', views.like_comment, name='like_comment'),
 	path('comment/<int:comment_id>/dislike', views.dislike_comment, name='dislike_comment'),
 	path('comment/comments/<int:commentcomment_id>/like', views.like_comment_on_comment, name='like_comment_on_comment'),
 	path('comment/comments/<int:commentcomment_id>/dislike', views.dislike_comment_on_comment, name='dislike_comment_on_comment'),

 	path('questions', views.QuestionList.as_view(), name='questions'),
 	path('<int:question_id>/comment', views.question_comments, name='question_comments'),
 	path('comment/<int:comment_id>', views.comments_on_comment, name='comments_on_comment')
 ]
