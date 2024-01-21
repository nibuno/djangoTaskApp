
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'items'


class TaskCreateView(CreateView):
    model = Task
    fields = ['content']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
