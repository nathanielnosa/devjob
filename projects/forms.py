from django.db.models import fields
from .models import *
from django.forms import ModelForm
from django import forms

class CreateProject(ModelForm):
  class Meta:
    model = Project
    fields = ['title', 'description','main_photo','demo', 'social_link', 'tags']
    widgets={
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class':'form-control'}),
      'main_photo':forms.FileInput(attrs={'class':'form-control'}),
      'demo': forms.TextInput(attrs={'class': 'form-control'}),
      'social_link': forms.TextInput(attrs={'class': 'form-control'}),
      'tags':forms.CheckboxSelectMultiple(),
      
    }
