from django.forms import ModelForm, TextInput, FileInput

from django import forms
from .models import Pin

class PinForm(forms.ModelForm):
    class Meta:
        
        model = Pin
        fields = ['title', 'description', 'pin']    

        # widgets = {
        #     'title': TextInput(),
        #     'pin': FileInput(),
        #     'description': TextInput(),
        # }