from django.forms import ModelForm
from django import forms
from .models import *
import os


class ApplicationForm(ModelForm):
    class Meta:
        model = Resume
        fields = ('email', 'first_name', 'last_name', 'age', 'education', 'cv', 'phone_number')

class CreateApplicationForm(ModelForm):
    class Meta:
        model = Resume
        fields = ('email', 'first_name', 'last_name', 'age', 'education', 'cv', 'phone_number')

    cv = forms.FileField()

    def clean_cv(self):
        uploaded_file = self.cleaned_data['cv']
        try:
            # create an cvField instance
            im = forms.cvField()
            # now check if the file is a valid cv
            im.to_python(uploaded_file)
        except forms.ValidationError:
            # file is not a valid cv;
            # so check if it's a pdf
            name, ext = os.path.splitext(uploaded_file.name)
            if ext not in ['.pdf', '.PDF']:
                raise forms.ValidationError("Only cvs and PDF files allowed")
        return uploaded_file