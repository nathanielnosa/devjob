from django.http import request
from django.shortcuts import render
from .models import Profile
# Create your views here.


def profiles(request):
  profiles = Profile.objects.all()
  
  context = {
    'show':profiles
  }
  return render(request, 'users/profiles.html', context)


def profile(request,id):
  profile = Profile.objects.get(pk=id)
  skillone =  profile.skill_set.exclude(description__exact="")
  skilltwo =  profile.skill_set.filter(description="")
  context = {
    'show':profile,
    'skillone':skillone,
    'skilltwo':skilltwo
  }
  return render(request, 'users/profile.html', context)
