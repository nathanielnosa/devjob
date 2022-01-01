from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django import forms
from . models import Profile, Skill, Message, Subscribers


class CreateUser(UserCreationForm):
  password1 = forms.CharField(
  label=("Password"),
  widget=forms.PasswordInput(
      attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
  password2 = forms.CharField(
    label=("Password confirmation"),
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'})
  )
  
  class Meta:
    model = User
    fields = ['first_name','email','username','password1','password2']
    labels = {
      'first_name':'Name',
    }
    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'e.g: John Doe'}),
        'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'e.g: nathaniel@gmail.com'}),
        'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'eg: Nosa'}),
    }


class Editprofile(ModelForm):
  class Meta:
    model = Profile
    fields = ['name', 'email', 'username', 'headline', 'bio', 'location', 'profile_pix','social_git', 'social_twitter', 'social_facebook', 'social_instagram', 'social_linkedin', 'Social_website']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'headline': forms.TextInput(attrs={'class': 'form-control'}),
        'bio': forms.Textarea(attrs={'class': 'form-control'}),
        'location': forms.TextInput(attrs={'class': 'form-control'}),
        'profile_pix': forms.FileInput(attrs={'class': 'form-control'}),
        'social_git': forms.TextInput(attrs={'class': 'form-control'}),
        'social_twitter': forms.TextInput(attrs={'class': 'form-control'}),
        'social_facebook': forms.TextInput(attrs={'class': 'form-control'}),
        'social_instagram': forms.TextInput(attrs={'class': 'form-control'}),
        'social_linkedin': forms.TextInput(attrs={'class': 'form-control'}),
        'Social_website': forms.TextInput(attrs={'class': 'form-control'}),
    }


class SkillForm(ModelForm):
  class Meta:
    model = Skill
    fields = '__all__'
    exclude = ['owner']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g React'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'e.g I have 3 years skills on react'}),
    }


class SendMessage(ModelForm):
  class Meta:
    model = Message
    fields = ['name','email','subject','body']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g Nathaniel Nosa'}),
      'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'e.g NathanielNosa@gmail.com'}),
      'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g Lookin For A Developer'}),
      'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'e.g I need a web dev...'}),
    }


class Subscribe(ModelForm):
  class Meta:
    model = Subscribers
    fields = ['name','email']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g Nathaniel Nosa'}),
      'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'e.g NathanielNosa@gmail.com'}),
    }