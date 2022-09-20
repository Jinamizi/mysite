from django.contrib import admin
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.urls import reverse

from myblog.models import Article, Author

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['__str__','author','date_published','is_draft'] #display other data in the admin change list
	search_fields = ['title']
	'''list_display = ['title', 'author_link', 'date_published', 'is_draft']

	#list_display is not limited to the model fields and properties. It can also be a method of your ModelAdmin
	def author_link(self, obj):
		author = obj.author
		opts = author._meta
		route = '{}_{}_change'.format(opts.app_label, opts.model_name)
		author_edit_url = reverse(route, args=[author.pk])
		return format_html('<a{}>{}</a>',flatatt({'href':author_edit_url}), author.first_name)

	#Set the column name in the change list
	author_link.short_description = "Author"
	#set the field to use when ordering using this column
	author_link.admin_order_field = 'author__firstname'''

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display= ['first_name', 'last_name']
	search_fields = ['first_name', 'last_name']