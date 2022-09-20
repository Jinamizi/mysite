from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404

from .models import *
from .forms import *

class IndexView(generic.ListView):
	template_name = 'bandcollections/index.html'
	context_object_name = 'bands'

	def get_queryset(self):
		return Band.objects.all()

class BandView(generic.DetailView):
	'''Displays the information of a given band.'''
	model = Band
	template_name = 'bandcollections/band.html'

class RegisteredBand(generic.DetailView):
	'''Displays information after successfull registration of a band'''
	model = Band
	template_name = 'bandcollections/registration_successful.html'

def musicianView(request, band_id, musician_id):
	band = get_object_or_404(Band, band_id)
	try:
		musician = band.musician_set.get(pk=musician_id)
	except (Musician.DoesNotExist):
		raise Http404("Musician does not Exist")
	else:
		render(request, 'bandcollections/musician.html', {'musician':musician})

def registerBand(request):
	'''registers a new band and saves it. displays a page to register band. displays a page if registration was successfully'''
	if request.method == 'POST':
		form = BandForm(request.POST)

		if form.is_valid():
			band = form.save(commit=False)
			band.date_formed = timezone.now()
			band.save()
			return HttpResponseRedirect(reverse('bandcollections:registration_successful', args = (band.id,)))
	else:
		form = BandForm()
	return render(request, 'bandcollections/register.html', {'form':form})

def join(request, band_id):
	'''allows one to join the band with the given band_id. if join was successfull, displays a joined_successful page.'''
	band = get_object_or_404(Band, pk=band_id)
	if request.method == 'POST':
		form = JoinForm(request.POST)

		if form.is_valid():
			musician = band.musician_set.create(stage_name=form.cleaned_data['stage_name'],\
				real_name =form.cleaned_data['real_name'])
			return render(request, 'bandcollections/joined_successfully.html', {'band':band, 'musician':musician})

	else:
		form = JoinForm()
	return render(request, 'bandcollections/join.html', {'form':form, 'band':band})	
		