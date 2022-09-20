from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

from .models import Student, Person
from .forms import StudentForm, PersonForm, Example0Form

def registerStudent(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)

		if form.is_valid():
			student = form.save()
			return HttpResponseRedirect(reverse('examples:student_display', args=(student.id,)))
			#render(request, 'examples/studentDisplay.html', {'student': student})
	else:
		form = StudentForm()
	return render(request, 'examples/students_register.html', {'form': form})

def example0(request):
	if request.method == 'POST':
		form = Example0Form(request.POST)

		if form.is_valid():
			value = form.cleaned_data['even_field']
			return HttpResponse('You entered %s' % value)
	else:
		form = Example0Form()
	return render(request, 'examples/example0.html', {'form': form})


class StudentDisplay(generic.DetailView):
	model = Student
	template_name = 'examples/studentDisplay.html'

