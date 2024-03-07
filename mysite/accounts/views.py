from django.contrib.auth import login, authenticate
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

    def post(self, request, *args, **kwargs):
        """ユーザー作成後、ログインする

        NOTE: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
              の内容を元に実装
        """
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("task_list")
        else:
            return super().post(request, *args, **kwargs)
