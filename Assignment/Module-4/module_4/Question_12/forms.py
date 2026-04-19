from django import forms
from .models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model=doctorprofile
        fields='__all__'