from projects.models import Project
from django.shortcuts import redirect, render
from .forms import CreateProject
# Create your views here.

def projects(request):
  show = Project.objects.all()
  context = {
    'show':show,
  }
  return render(request, 'projects/projects.html',context)

def project(request,id):
  show = Project.objects.get(pk=id)
  context = {
    'show':show,
  }
  return render(request, 'projects/project.html', context)

def createproject(request):
  form = CreateProject()

  if request.method == 'POST':
    form = CreateProject(request.POST, request.FILES)
    if form.is_valid:
      form.save()
      return redirect('projects')
  context = {
    'form':form,
  }
  return render(request, 'projects/create.html',context)

def updateproject(request, id):
  update =  Project.objects.get(pk=id)
  form = CreateProject(instance= update)

  if request.method == 'POST':
    form = CreateProject(request.POST, request.FILES, instance=update)
    if form.is_valid:
      form.save()
      return redirect('projects')
  context = {
    'form':form,
  }
  return render(request, 'projects/create.html',context)


def deleteproject(request, id):
  delete = Project.objects.get(pk=id)
  if request.method == "POST":
    delete.delete()
    return redirect('projects')

  context = {
    'delete':delete
  }
  return render(request, 'projects/delete.html',context)
