from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'items'


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Task
    fields = ['content']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('task_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.created_user = self.request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Task
    success_url = reverse_lazy('task_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
