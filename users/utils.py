from .models import Profile, Skill

from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def searchProfile(request):
  my_search = ''
  if request.GET.get('search'):
    my_search = request.GET.get('search')
    print(my_search)

  skills = Skill.objects.filter(name__icontains = my_search)
  profiles = Profile.objects.distinct().filter(
    Q(name__icontains=my_search) |
    Q(headline__icontains=my_search)|
    Q(skill__in=skills)
    )

  return profiles, my_search



# pagination
def paginateProfiles(request, profiles, result):

  page = request.GET.get('page')
  paginator = Paginator(profiles, result)

  try:
    profiles = paginator.page(page)
  except PageNotAnInteger:
    page = 1
    profiles = paginator.page(page)
  except EmptyPage:
    page = paginator.num_pages
    profiles = paginator.page(page)

  leftIndex = (int(page)-1)
  if leftIndex < 1:
    leftIndex = 1
  rightIndex = (int(page)+3)
  if rightIndex > paginator.num_pages:
    rightIndex = paginator.num_pages + 1
  custom_range = range(leftIndex, rightIndex)

  return custom_range, profiles
