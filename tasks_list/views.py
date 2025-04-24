from django.views.generic import CreateView, ListView
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

  def form_valid(self, form):
      # Assigner l'utilisateur connecté à l'attribut author
      form.instance.author = self.request.user
      return super().form_valid(form)


class CategoryListView(ListView):
  model= Category
  template_name= ('tasks_list/category_list.html')
  context_object_name= 'categories'
  



class ProjectCreateView(CreateView):
  model= Project
  form_class= CategoryCreationForm
  template_name= ('tasks_list/project_form.html')
  success_url=reverse_lazy('home')



class TaskListView(ListView):
  model= Task
  template_name= ('tasks_list/task_list.html')
  context_object_name= 'tasks'
  ordering= ['-creation_date']