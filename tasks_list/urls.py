from django.urls import path
from .views import TaskCreateView, CategoryCreateView, ProjectCreateView, CategoryListView

urlpatterns = [
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('task_create/', TaskCreateView.as_view(), name='task_create'),
    path('project_create/', ProjectCreateView.as_view(), name='project_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    #path('', TaskListView.as_view(), name='task_list'),
    #path('task/<slug:slug>/', TaskDetailView.as_view(), name='task_detail'),
    #path('task/<slug:slug>/update/', TaskUpdateView.as_view(), name='task_update'),
    #path('task/<slug:slug>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]