from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import ComplaintForm
from .models import Complaint

class ComplaintView(View):
    def get(self, request):
        return render(request, 'complaints/complaint.html', {'form': ComplaintForm()})

    def post(self, request):
        form = ComplaintForm(request.POST)
        if form.is_valid():
            Complaint.objects.create(message=form.cleaned_data['message'])
            return HttpResponseRedirect(reverse('thanks'))
        else:
            return render(request, 'complaints/complaint.html', {'form': ComplaintForm()})
