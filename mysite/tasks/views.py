from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskSearchForm


class TaskListView(ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get("title")

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm(self.request.GET or None)
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Task
    fields = ["title", "content", "limit_date", "status"]
    template_name = "task/task_create.html"
    success_url = reverse_lazy("task_list")

    def post(self, request, *args, **kwargs):
        # NOTE: これを設定しないと、self.form_invalid(form)でエラーが発生する
        #       どういう風にすべきなのか、このままで良いのかは調査する
        self.object = None
        form = self.get_form()
        if form.is_valid():
            form.instance.created_user = self.request.user
            form.instance.updated_user = self.request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Task
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TaskEditView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Task
    fields = ["title", "content", "limit_date", "status"]
    template_name = "task/task_edit.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        task = form.save(commit=False)

        # 作成者は変更しない
        current_task = Task.objects.get(pk=self.kwargs["pk"])
        task.created_user = current_task.created_user

        task.updated_user = self.request.user
        task.save()
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    model = Task
    template_name = "task/task_detail.html"
