from django.contrib import admin

from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email' , 'date_joined', 'activity_count']
	search_fields = ['username', 'email']
	list_filter = ['date_joined']
