from django.contrib import admin

from . import models

@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
	list_display = ["name", "address", "city", "state_province", "country", "website"]
	search_fields = ["name", "address", "city", "state_province", "country", "website"]

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ["title", "publisher", "publication_date"]
	search_fields = ["title", "publisher"]

@admin.register(models.Author)
class BookAdmin(admin.ModelAdmin):
	list_display = ["salutation", "name", "email"]
	search_fields = ["title", "publisher"]