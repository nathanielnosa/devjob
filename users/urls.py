from django.urls import path
from .import views

urlpatterns =[
  path('', views.profiles, name='profiles'),
  path('profile/<str:id>/', views.profile, name='profile'),
  path('login', views.loginuser, name='login'),
  path('logout', views.logoutuser, name='logout'),
  path('register', views.registeruser, name='register'),
  path('register', views.registeruser, name='register'),
  path('account', views.useraccount, name='account'),
  path('editprofile', views.editprofile, name='editprofile'),
  path('createskill', views.createskill, name='createskill'),
  path('updateskill/<str:pk>/', views.updateskill, name='updateskill'),
  path('deleteskills/<str:pk>/', views.deleteskills, name='deleteskills'),

  path('inbox/', views.inbox, name='inbox'),
  path('message/<str:id>/', views.viewmesg, name='message'),
  path('sendmessage/<str:pk>/', views.sendmessage, name='sendmessage'),
  
  path('subscribers/', views.Mailformview, name='subscribers'),

  ]
