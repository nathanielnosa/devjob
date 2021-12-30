from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def searchProject(request):
  my_search = ''
  if request.GET.get('search'):
    my_search = request.GET.get('search')
    print(my_search)

  tags = Tag.objects.filter(name__icontains = my_search)
  show = Project.objects.distinct().filter(
    Q(title__icontains=my_search) |
    Q(description__icontains=my_search)|
    Q(owner__name__icontains=my_search)|
    Q(tags__in=tags)
    )

  return show, my_search

# pagination
def paginateProject(request, show, result):

  page = request.GET.get('page')
  paginator = Paginator(show, result)

  try:
    show = paginator.page(page)
  except PageNotAnInteger:
    page = 1
    show = paginator.page(page)
  except EmptyPage:
    page = paginator.num_pages
    show = paginator.page(page)

  leftIndex = (int(page)-1)
  if leftIndex < 1:
    leftIndex = 1
  rightIndex = (int(page)+3)
  if rightIndex > paginator.num_pages:
    rightIndex = paginator.num_pages + 1
  custom_range = range(leftIndex, rightIndex)

  return custom_range, show
