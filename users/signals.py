from . models import *
from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete

from django.core.mail import send_mail
from django.conf import settings


def createProfile(sender, instance, created, **kwargs):
  if created:
    user = instance

    profile = Profile.objects.create(
        user=user,
        username=user.username,
        email=user.email,
        name=user.first_name,
    )
    subject = 'Welcome To DevJob'
    body = f'Greetings from DevJob Web Services, \n Thank you for signing up for DevJob Support. You now have access to DevJob platforms. \n If you interact with DevJob programmatically, you must provide your full information after signup to verify who you are and whether you have permission to access the resources you are requesting.\n Welcome to the DevJob Web Services community!\n —The DevJob Web Services Team'
    send_mail(
          subject,
          body,
          settings.EMAIL_HOST_USER,
          [profile.email],
          fail_silently= False
        )


def updateProfile(sender, instance, created, **kwargs):
  profile = instance
  user = profile.user
  if created == False:
    user.username = profile.username
    user.email = profile.email
    user.first_name = profile.name
    user.save()

  

def deleteProfile(sender, instance, **kwargs):
  user = instance.user
  user.delete()


post_save.connect(createProfile, sender=User)

post_save.connect(updateProfile, sender=Profile)

post_delete.connect(deleteProfile, sender=Profile)
