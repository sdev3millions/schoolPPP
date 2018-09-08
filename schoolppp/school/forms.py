from django import forms
from .models import SchoolData,Schools

class SchoolForm(forms.ModelForm):
    class Meta:
        model = SchoolData
        fields="__all__"