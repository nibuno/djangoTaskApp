from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='todo_delete'),
]
