from django import forms
from .models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model=doctorinfo
        fields='__all__'