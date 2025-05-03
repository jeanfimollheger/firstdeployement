from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Task, Category, Project
from .forms import TaskCreationForm, CategoryCreationForm, ProjectCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
"""Ces mixins assurent que l'utilisateur est connecté et qu'il passe un test 
  spécifique avant d'accéder à la vue"""
from .models import Category


class CategoryCreateView(CreateView):
  model= Category
  form_class= CategoryCreationForm
  template_name= ('tasks_list/category_form.html')
  success_url=reverse_lazy('home')

  def form_valid(self, form):
      # Assigner l'utilisateur connecté à l'attribut author
      form.instance.author = self.request.user
      return super().form_valid(form)
  
  def get_context_data(self,*args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['action'] = 'create'
    return context


class CategoryDetailView(LoginRequiredMixin, UserPassesTestMixin,DetailView):
  model= Category
  template_name= ('tasks_list/category_detail.html')
  context_object_name= 'category'

  def get_queryset(self):
      # Filtrer les catégories par l'utilisateur connecté
      return Category.objects.filter(author=self.request.user)

  def test_func(self):
      category = self.get_object()
      return self.request.user == category.author
  

class CategoryListView(ListView):
  model= Category
  template_name= ('tasks_list/category_list.html')
  context_object_name= 'categories'

  def get_queryset(self):
      # Filtrer les catégories par l'utilisateur connecté
      return Category.objects.filter(author=self.request.user)


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
  """Ces mixins assurent que l'utilisateur est connecté et qu'il passe un test 
  spécifique avant d'accéder à la vue"""
  model= Category
  form_class= CategoryCreationForm
  template_name= ('tasks_list/category_form.html')
  success_url=reverse_lazy('home')

  def get_queryset(self):
     return Category.objects.filter(author=self.request.user)
  
  def test_func(self):
      category = self.get_object()
      return self.request.user == category.author
  
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['action'] = 'update'
    return context


class ProjectCreateView(CreateView):
  model= Project
  form_class= ProjectCreationForm
  template_name= ('tasks_list/project_form.html')
  success_url=reverse_lazy('home')

  def form_valid(self, form):
    # Assigner l'utilisateur connecté à l'attribut author
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  def get_context_data(self,*args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['action'] = 'create'
    return context

class ProjectDetailView(LoginRequiredMixin, UserPassesTestMixin,DetailView):
  model= Project
  template_name= ('tasks_list/project_detail.html')
  context_object_name= 'project'

  def get_queryset(self):
      # Filtrer les projets par l'utilisateur connecté
      return Project.objects.filter(author=self.request.user)

  def test_func(self):
      project = self.get_object()
      return self.request.user == project.author


class ProjectListView(ListView):
  model= Project
  template_name= ('tasks_list/project_list.html')
  context_object_name= 'projects'

  def get_queryset(self):
      # Filtrer les projets par l'utilisateur connecté
      return Project.objects.filter(author=self.request.user)
  

class TaskCreateView(CreateView):
  model= Task
  form_class= TaskCreationForm
  template_name= ('tasks_list/task_form.html')
  success_url=reverse_lazy('home')

  def get_form_kwargs(self):
      kwargs = super().get_form_kwargs()
      kwargs['user'] = self.request.user
      return kwargs
  
  def form_valid(self, form):
    # Assigner l'utilisateur connecté à l'attribut author
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  def get_context_data(self,*args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    # Filtrer les querysets des catégories et projets en fonction de l'utilisateur connecté
    context['action'] = 'create'
    return context
  

class TaskListView(ListView):
  model= Task
  template_name= ('tasks_list/task_list.html')
  context_object_name= 'tasks'
  ordering= ['-creation_date']