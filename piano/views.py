from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *

def search(request):
	form = SearchForm() #create a blank form
	context = {'id':'','name':'', 'rat':''}

	#if this is a POST request we need to process the form data
	if request.method == 'POST':
		form = SearchForm(request.POST)
		cellinfo['id'] = 3333
		cellinfo['name'] = "name"
		cellinfo['rat']="3G"

	else:
		pass

	context = {'form':form, 'cellinfo':cellinfo}
	return render(request, "piano/index.html", context)

