from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import ComplimentForm
from .models import Compliment

class ComplimentView(View):
	def get(self, request):
		return render(request, 'compliments/compliment.html', {'form': ComplimentForm()})

	def post(self, request):
		form = ComplimentForm(request.POST)
		if form.is_valid():
			Compliment.objects.create(message=form.cleaned_data['message'])
			return HttpResponseRedirect(reverse('thanks'))
		else:
			return render(request, 'compliments/compliment.html', {'form': ComplimentForm()})