from projects.models import Project
from django.shortcuts import redirect, render
from .forms import CreateProject,CreateReview

from .utils import searchProject,paginateProject


from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def projects(request):
  show, my_search = searchProject(request)
  custom_range, show = paginateProject(request,show, 6)
 
  context = {
    'show':show,
    'my_search':my_search,
    'custom_range': custom_range,
  }
  return render(request, 'projects/projects.html',context)

def project(request,id):
  show = Project.objects.get(pk=id)
  form = CreateReview()
  if request.method == 'POST':
    form = CreateReview(request.POST)
    review = form.save(commit=False)
    review.project = show
    review.owner = request.user.profile
    review.save()

    show.getVote
    
    messages.success(request, 'You just made a post and vote.')
    return redirect('project', id =show.id)
  context = {
    'show':show,
    'form':form
  }
  return render(request, 'projects/project.html', context)


@login_required(login_url="login")
def createproject(request):
  profile = request.user.profile
  form = CreateProject()

  if request.method == 'POST':
    form = CreateProject(request.POST, request.FILES)
    if form.is_valid:
      project = form.save(commit=False)
      project.owner = profile
      project.save()
      messages.success(request, 'Project Added Successfully.')


      return redirect('account')
  context = {
    'form':form,
  }
  return render(request, 'projects/create.html',context)


@login_required(login_url="login")
def updateproject(request, id):
  profile = request.user.profile
  update =  profile.project_set.get(pk=id)
  form = CreateProject(instance= update)

  if request.method == 'POST':
    form = CreateProject(request.POST, request.FILES, instance=update)
    if form.is_valid:
      form.save()
      messages.success(request, 'Project Update Successfully.')

  
      return redirect('account')
  context = {
    'form':form,
  }
  return render(request, 'projects/create.html',context)

@login_required(login_url="login")
def deleteproject(request, id):
  profile = request.user.profile
  delete = profile.project_set.get(pk=id)
  if request.method == "POST":
    delete.delete()
    messages.success(request, 'user delete project successfully.')

    return redirect('projects')

  context = {
    'delete':delete
  }
  return render(request, 'partial/delete.html',context)
