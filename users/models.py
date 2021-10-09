from django.db import models

from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save
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
    return str(self.user.username)

class Skill(models.Model):
  owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True, blank=True)
  description = models.TextField(null=True, blank=True) 
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.name)



def updateProfile(sender, instance, created, **kwargs):
  print('data profile updated ..')

post_save.connect(updateProfile, sender = Profile)

