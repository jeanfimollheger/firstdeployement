from django import forms
from .models import Task, Category, Project

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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(author=user)
            self.fields['project'].queryset = Project.objects.filter(author=user)
            
             
class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter category name'}),
        }
        labels = {
            'name': 'Category Name',
        }
        help_texts = {
            'name': 'Please provide a name for the category.',
        }

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'target_date_project']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter project name'}),
            'target_date_project': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Project Name',
            'target_date_project': 'Target Date',
        }
        help_texts = {
            'name': 'Please provide a name for the project.',
            'target_date_project': 'Select the target date for this project.',
        }