from django import forms
from .models import Task

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'done', 'category', 'project','task_target_date']
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Enter task description'}),
            'done': forms.CheckboxInput(),
            'category': forms.Select(),
            'project': forms.Select(),
            'task_target_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'description': 'Task Description',
            'done': 'Completed',
            'category': 'Category',
            'project': 'Project',
            'task_target_date': 'Target Date',
        }
        help_texts = {
            'description': 'Please provide a brief description of the task.',
            'done': 'Check if the task is completed.',
            'category': 'Select the category for this task.',
            'project': 'Select the project associated with this task.',
            'task_target_date': 'Select the target date for this task.',
        }