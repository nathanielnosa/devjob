from django.http import request
from django.shortcuts import render, redirect

from django.contrib.auth import login,logout,authenticate
from . forms import CreateUser, Editprofile, SkillForm, SendMessage, UserSubscribe
from django.contrib.auth.models import User
from .models import Message, Profile, Skill

from .utils import searchProfile, paginateProfiles
from django.db.models import Q


from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.


# login users
def loginuser(request):
  page = 'login'
  if request.user.is_authenticated:
    return redirect('profiles')

  if request.method == 'POST':
    username =  request.POST['username'].lower()
    password =  request.POST['password']

    try:
      user = User.objects.get(username = username)
    except:
      messages.warning(request, 'Username does not exit.')

    user = authenticate(request, username = username, password = password)

    if user is not None:
      login(request, user)
      return redirect(request.GET['next'] if 'next' in request.GET else 'account')
    else:
      messages.warning(request, 'Username or Password does not match.')


  return render(request, 'users/loginregister.html')

# logout user
def logoutuser(request):
  logout(request)
  messages.success(request, 'User logged out.')
  return redirect('login')

# user registration
def registeruser(request):
  page = 'register'
  form = CreateUser()
  if request.method == 'POST':
    form = CreateUser(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      if User.objects.filter(email=user.email).exists():
        messages.warning(request, 'Email is taken')
        return redirect('register')
      user.save()
      messages.success(request, 'User Registered Successful.')
      login(request, user)
      return redirect('editprofile')
    else:
      messages.warning(request, 'User Registration Failed.')

  context={
    'page':page,
    'form':form,
  }
  return render(request, 'users/loginregister.html',context)

# user profiles
def profiles(request):
  profiles, my_search = searchProfile(request)
  custom_range, profiles = paginateProfiles(request, profiles, 6)

  context = {
    'show':profiles,
    'my_search':my_search,
    'custom_range':custom_range,
  }
  return render(request, 'users/profiles.html', context)


# user single profile
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

# user account page
@login_required(login_url="login")
def useraccount(request):
  profile = request.user.profile
  allskill =  profile.skill_set.all()
  project =  profile.project_set.all()
  context = {
    'profile':profile,
    'skillone':allskill,
    'project':project
  }

  return render(request, 'users/account.html', context)

# edit user profile
@login_required(login_url="login")
def editprofile(request):
  profile = request.user.profile
  form = Editprofile(instance=profile)
  if request.method == 'POST':
    form = Editprofile(request.POST, request.FILES, instance = profile)
    if form.is_valid():
      form.save()

      return redirect('account')
  context={
    'form':form
  }
  return render(request, 'users/editprofile.html', context)


# creating skill
@login_required(login_url="login")
def createskill(request):
  profile = request.user.profile
  form = SkillForm()
  if request.method == 'POST':
    form = SkillForm(request.POST)
    if form.is_valid():
      skill = form.save(commit= False)
      skill.owner = profile
      skill.save()
      messages.success(request, 'skills added successfully.')

    return redirect('account')

  context={
    'form':form
  }
  return render(request, 'users/skillform.html', context)

@login_required(login_url="login")
def updateskill(request,pk):
  profile = request.user.profile
  currentskill = profile.skill_set.get(id=pk)
  form = SkillForm(instance=currentskill)
  if request.method == 'POST':
    form = SkillForm(request.POST, instance=currentskill)
    if form.is_valid():
      form.save()
      messages.success(request, 'skills updated.')
    return redirect('account')
    
  context={
    'form':form
  }
  return render(request, 'users/skillform.html', context)



@login_required(login_url="login")
def deleteskills(request, pk):
  profile = request.user.profile
  delete = profile.skill_set.get(id =pk)
  if request.method == "POST":
    delete.delete()
    messages.success(request, 'user delete skill successfully.')
    return redirect('account')

  context = {
    'delete':delete
  }

  return render(request, 'partial/delete.html', context)



@login_required(login_url="login")
def inbox(request):
  profile =request.user.profile
  msg = profile.messages.all()
  unreadMsg = msg.filter(is_read=False).count()
  context = {
    'unreadmsg':unreadMsg,
    'msg':msg
  }
  return render(request, 'users/inbox.html', context)

@login_required(login_url="login")
def viewmesg(request, id):
  profile =request.user.profile
  msg = profile.messages.get(pk=id)
  if msg.is_read == False:
    msg.is_read = True
    msg.save()
  context = {
    'msg':msg
  }
  return render(request, 'users/message.html', context)


def sendmessage(request, pk):
  recipient = Profile.objects.get(id=pk)
  form = SendMessage()

  try:
    sender = request.user.profile
  except:
    sender = None
  
  if request.method == 'POST':
    form = SendMessage(request.POST)
    if form.is_valid():
      message = form.save(commit=False)
      message.sender = sender
      message.recipient = recipient
      
      if sender:
        message.name =sender.name
        message.email =sender.email
      message.save()

      messages.success(request, 'Your message was successfully sent.')
      
      return redirect('profile', id = recipient.pk)

  context = {
    'form':form,
    'recipient':recipient
  }
  return render(request, 'users/sendmessage.html', context)


def Usersubscriber(request):
  form = UserSubscribe()
  if request.method == 'POST':
    form = UserSubscribe(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Congrats! You have subscribe.')
  context = {
    'form':form
  }
  return render(request, 'partial/_footer.html', context)

