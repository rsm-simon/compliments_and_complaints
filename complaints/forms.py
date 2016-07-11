# coding=utf-8
from django import forms

from .models import Complaint

class ComplaintForm(forms.Form):
    message = forms.CharField(label="Поплака", widget=forms.Textarea)
