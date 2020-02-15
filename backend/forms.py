from django import forms
from .models import *


class DocumentForm(forms.ModelForm):
    debit_sum = forms.FloatField(required=False)
    credit_sum = forms.FloatField(required=False)
    difference = forms.FloatField(required=False)