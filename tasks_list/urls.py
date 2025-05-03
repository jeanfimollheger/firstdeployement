from django.urls import path
from .views import CategoryCreateView,CategoryDetailView, CategoryUpdateView, CategoryListView 
from .views import ProjectCreateView, ProjectDetailView, ProjectListView, TaskCreateView, TaskListView
urlpatterns = [
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_detail/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category_update/<slug:slug>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('project_create/', ProjectCreateView.as_view(), name='project_create'),
    path('project_detail/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project_list/', ProjectListView.as_view(), name='project_list'),
    path('task_create/', TaskCreateView.as_view(), name='task_create'),
    path('', TaskListView.as_view(), name='task_list'),
    #path('task/<slug:slug>/', TaskDetailView.as_view(), name='task_detail'),
    #path('task/<slug:slug>/update/', TaskUpdateView.as_view(), name='task_update'),
    #path('task/<slug:slug>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]