from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView

from . import models,forms

class LoginView(FormView):
	template_name = 'actilist/login.html'
	form_class = forms.LoginForm
	#success_url = reverse('actilist:activities', args)

	def get(self, request):
		if 'user_id' in request.session:
			username = models.User.objects.get(pk=request.session['user_id'])
			return HttpResponseRedirect(reverse('actilist:user-activities', args=(username,)))
		else:
			return render(request, self.template_name, {'form':self.get_form_class()})

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			user = models.User.objects.get(username=form.cleaned_data['username'])
			request.session['user_id'] = user.id
			return HttpResponseRedirect(reverse('actilist:user-activities', args=(user.name,)))
		else:
			return super().form_invalid(form)


class CreateAccountView(FormView):
	template_name = 'actilist/signup.html'
	form_class = forms.CreateAccountForm
	#success_url = reverse_lazy('actilist:user-profile', args=(self.user_id,))

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			user = form.save()
			request.session['user_id'] = user.id
			return user.get_absolute_url()
		else:
			return super().form_invalid(form)

class UserActivitiesList(ListView):
	template_name = 'actilist/activities_list.html'

	def get_queryset(self):
		self.user = get_object_or_404(models.User, name=self.kwargs['username'])
		return Activity.objects.filter(user=self.user)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = self.user 
		return context




