from django import forms
from .models import SchoolData,Schools

class SchoolDataForm(forms.ModelForm):
    class Meta:
        model = SchoolData
        fields="__all__"
class SchoolForm(forms.ModelForm):
    class Meta:
        model = Schools
        fields = "__all__"

