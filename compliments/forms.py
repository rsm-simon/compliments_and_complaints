# coding=utf-8
from django import forms

from .models import Compliment

class ComplimentForm(forms.Form):
    message = forms.CharField(label="Пофалба", widget=forms.Textarea)