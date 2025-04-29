from django.db import models
from django.utils.text import slugify
from datetime import date, timedelta
from django.conf import settings

from members.models import Member


def default_target_date():
  return date.today() + timedelta(days=1)


# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, blank=True)
  author=models.ForeignKey(settings.AUTH_USER_MODEL, 
                           on_delete=models.CASCADE, 
                           related_name="author_categories", 
                           null=True, 
                           blank=True
                          )
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return f'{self.name} ({self.pk})'
  

class Project(models.Model):   
  name=models.CharField(max_length=100, unique=True)
  slug=models.SlugField(max_length=100, unique=True, blank=True)
  target_date_project = models.DateField(default=default_target_date)
  author=models.ForeignKey(settings.AUTH_USER_MODEL, 
                          on_delete=models.CASCADE, 
                          related_name="author_projects", 
                          null=True, 
                          blank=True
                          )
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return f'{self.slug}'


class Task(models.Model):
  description=models.CharField(max_length=200, blank=False, unique=True)
  slug=models.SlugField(max_length=200, unique=True, blank=True)
  done=models.BooleanField(default=False)
  creation_date=models.DateField(default=date.today)
  author=models.ForeignKey(settings.AUTH_USER_MODEL, 
                           on_delete=models.CASCADE, 
                           related_name="author_tasks", 
                           null=True, 
                           blank=True
                          )
  category=models.ForeignKey(Category, 
                             on_delete=models.CASCADE, 
                             related_name="category_tasks", 
                             null=True, 
                             blank=True
                            )
  project=models.ForeignKey(Project, 
                            on_delete=models.CASCADE, 
                            related_name="project_tasks", 
                            null=True, 
                            blank=True
                           )
  task_target_date = models.DateField(default=default_target_date)
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.description)
    super().save(*args, **kwargs)