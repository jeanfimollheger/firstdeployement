from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .models import Task
from .forms import TaskCreationForm

class TaskCreateView(CreateView):
  model= Task
  form_class= TaskCreationForm
  template_name= ('tasks_list/task_form.html')
  success_url=reverse_lazy('home')
#urls.pt => path('namemodel/create', NameModelCreateView.as_view(), name='namemodel-create'),

#forms.py

# Create your views here.
