from django.db import models

from django.contrib.auth.models import User
import uuid

from django.db.models.fields import EmailField


# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank= True)
  name = models.CharField(max_length=200, null=True, blank= True)
  username = models.CharField(max_length=200, null=True, blank=True)
  email = models.CharField(max_length=200, null=True, blank=True)
  headline = models.CharField(max_length=200, null=True, blank= True)
  bio = models.TextField()
  location = models.CharField(max_length=200,null=True, blank=True)
  profile_pix = models.ImageField(upload_to='profiles/', default="profiles/avartar.png", null=True, blank=True)
  social_git = models.CharField(max_length=200, null=True, blank=True)
  social_twitter = models.CharField(max_length=200, null=True, blank=True)
  social_facebook = models.CharField(max_length=200, null=True, blank=True)
  social_instagram = models.CharField(max_length=200, null=True, blank=True)
  social_linkedin = models.CharField(max_length=200, null=True, blank=True)
  Social_website = models.CharField(max_length=200, null=True, blank=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
  created = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return str(self.username)

class Skill(models.Model):
  owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True, blank=True)
  description = models.TextField(null=True, blank=True) 
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.name)


class Message(models.Model):
  sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null= True, blank=True)
  recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null= True, blank=True, related_name='messages')
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  is_read = models.BooleanField(default=False, null= True)
  subject=models.CharField(max_length=250)
  body = models.TextField()
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)
  created = models.DateTimeField(auto_now_add=True)
 
  class Meta:
    ordering = ['is_read', '-created']

  def __str__(self):
    return self.subject

  

