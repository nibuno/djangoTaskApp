from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskSearchForm, TaskCreateForm, TaskEditForm
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

import logging

logging.basicConfig(level=logging.INFO)


class TaskListView(ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()

        # 初期表示時は何をすべきか表示したいので未着手、進行中のタスクを表示する
        if not self.request.GET:
            queryset = queryset.filter(status__in=[0, 1]).order_by("order")
            return queryset

        title = self.request.GET.get("title")
        content = self.request.GET.get("content")
        statuses = self.request.GET.getlist("status")
        limit_date = self.request.GET.get("limit_date")

        # FIXME: title, contentを1つの検索フォームで検索できるようにする
        if title:
            queryset = queryset.filter(title__icontains=title)
        if content:
            queryset = queryset.filter(content__icontains=content)
        if statuses:
            queryset = queryset.filter(status__in=statuses)
        if limit_date:
            queryset = queryset.filter(limit_date__lte=limit_date)

        queryset = queryset.order_by("order")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm(self.request.GET or None)
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Task
    form_class = TaskCreateForm
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

            logging.info(f"TaskCreateView:post:form.instance: {form.instance}")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Task
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        logging.info(f"TaskDeleteView:get:request: {request}")
        return self.post(request, *args, **kwargs)


class TaskEditView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Task
    form_class = TaskEditForm
    template_name = "task/task_edit.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        task = form.save(commit=False)

        # 作成者は変更しない
        current_task = Task.objects.get(pk=self.kwargs["pk"])
        task.created_user = current_task.created_user

        task.updated_user = self.request.user
        task.save()

        logging.info(f"TaskEditView:form_valid:task: {task}")

        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    model = Task
    template_name = "task/task_detail.html"


@require_http_methods(["POST"])
def save_order(request):
    """タスクの並び順を保存する

    並び順が同じ場合、何もしない
    並び順が異なる場合、新しい並び順を保存する

    タスクの数が多い場合、処理時間がかかる可能性が高い
    """
    try:
        new_order = json.loads(request.body.decode("utf-8"))
        for idx, task_id in enumerate(new_order):
            task = Task.objects.get(pk=task_id)
            if task.order == idx:
                continue
            task.order = idx
            task.save()
            logging.info("task_id: %s, new_order: %s", task_id, idx)
        return JsonResponse({"status": "success", "new_order": new_order})
    except Exception as e:
        logging.exception("error")
        return JsonResponse({"status": "error", "message": str(e)})
