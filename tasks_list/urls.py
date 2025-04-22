from django.urls import path
from .views import TaskCreateView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    #path('', TaskListView.as_view(), name='task_list'),
    #path('task/<slug:slug>/', TaskDetailView.as_view(), name='task_detail'),
    #path('task/<slug:slug>/update/', TaskUpdateView.as_view(), name='task_update'),
    #path('task/<slug:slug>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]