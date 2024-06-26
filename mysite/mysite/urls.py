"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from accounts.views import CreateUserView

urlpatterns = [
    path('__debug__/', include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("task/", include("tasks.urls")),
    path("login/", views.LoginView.as_view(next_page="task_list"), name="login"),
    # TODO: TOPページを作成して、TOPページへのリダイレクトを設定する
    path("logout/", views.LogoutView.as_view(next_page="task_list"), name="logout"),
    path("signup/", CreateUserView.as_view(), name="signup"),
    path("__reload__/", include("django_browser_reload.urls")),
]
