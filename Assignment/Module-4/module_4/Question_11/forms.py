from django import forms
from .models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model=doctorrecord
        fields='__all__'