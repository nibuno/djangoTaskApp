from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDeleteView, TaskEditView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('edit/<int:pk>', TaskEditView.as_view(), name='task_edit'),
]
