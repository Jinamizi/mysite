from django.contrib import admin

from .models import *

class Band_tabular_information(admin.TabularInline):
	model = BandTI
	extra = 1

class Band_descriptive_information(admin.StackedInline):
	model = BandDI
	extra = 1		

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
	list_display = ['stage_name','date_formed', 'number_of_musicians', 'number_of_songs']
	search_fields = ['stage_name']

	#splitting the form into fieldsets
	fieldsets = [
		('', {'fields':['stage_name', 'date_formed']}),
	]

	inlines = [Band_tabular_information, Band_descriptive_information]

class MusicianTII(admin.TabularInline):
	model = MusicianTI 
	extra = 1

class MusicianDII(admin.StackedInline):
	model = MusicianDI
	extra = 1

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
	list_display = ['real_name', 'stage_name', 'band']
	search_fields = ['real_name', 'stage_name']
	inlines = [MusicianTII, MusicianDII]

class MusicTII(admin.TabularInline):
	model = MusicTI
	extra = 1

class MusicDII(admin.StackedInline):
	model = MusicDI 
	extra = 1

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
	list_display = ['title', 'band', 'date_produced', 'producer']
	search_fields = ['title', 'band', 'producer']
	inlines = [MusicTII, MusicDII]