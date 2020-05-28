from django import forms

from Cars.models import Car

class OrderingForm(forms.Form):
    ordering = forms.CharField()