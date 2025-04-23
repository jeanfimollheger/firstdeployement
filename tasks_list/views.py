from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .models import Task, Category, Project
from .forms import TaskCreationForm, CategoryCreationForm

class TaskCreateView(CreateView):
  model= Task
  form_class= TaskCreationForm
  template_name= ('tasks_list/task_form.html')
  success_url=reverse_lazy('home')


class CategoryCreateView(CreateView):
  model= Category
  form_class= CategoryCreationForm
  template_name= ('tasks_list/category_form.html')
  success_url=reverse_lazy('home')