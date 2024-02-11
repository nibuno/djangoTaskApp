from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect


class CreateUserView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        """ログイン済みの場合はタスク一覧ページにリダイレクトする"""
        if request.user.is_authenticated:
            return redirect("task_list")
        return super().get(request, *args, **kwargs)
