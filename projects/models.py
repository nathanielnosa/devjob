from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Project(models.Model):
  owner = models.ForeignKey(Profile,null=True, blank=True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  main_photo = models.ImageField(
      default="thumbnail.png", null=True, blank=True)
  demo = models.CharField(max_length=5000,null=True, blank=True)
  social_link = models.CharField(max_length=5000,null=True, blank=True)
  tags = models.ManyToManyField('Tag',blank=True)
  vote_ratio = models.IntegerField(default=0, null= True, blank= True)
  vote_total = models.IntegerField(default=0, null= True, blank= True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key= True, editable=False)
  created = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ['-vote_ratio','-vote_total','title']
  

  @property
  def reviewers(self):
    checkers = self.review_set.all().values_list('owner__id', flat=True)
    return checkers

    
  @property
  def getVote(self):
    reviews = self.review_set.all()
    upVotes = reviews.filter(vote = 'up').count()
    totalVotes = reviews.count()

    ratio = (upVotes /totalVotes) * 100
    self.vote_ratio = ratio
    self.vote_total = totalVotes
    self.save()



class Tag(models.Model):
  name = models.CharField(max_length=300, null= True, blank= True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key= True, editable=False)
  created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name

class Review(models.Model):
  VOTE_TYPE= (
    ('up','Up Vote'),
    ('down','Down Vote'),
  )
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  body = models.TextField(null=True, blank=True)
  vote = models.CharField(max_length=300, choices= VOTE_TYPE)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key= True, editable=False)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = [['owner','project']]
   
  def __str__(self):
      return self.vote
