from django.contrib import admin

from . import models

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
	fields = ['username', 'password']
	list_display = ['username', 'password']