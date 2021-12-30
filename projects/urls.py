from django.urls import path
from .import views

urlpatterns =[
  path('', views.projects, name='projects'),
  path('project/<str:id>/', views.project, name='project'),
  path('createproject', views.createproject, name='createproject'),
  path('updateproject/<str:id>/', views.updateproject, name='updateproject'),
  path('deleteproject/<str:id>/', views.deleteproject, name='deleteproject'),
  ]
