from django.urls import path
from .views import (
    TaskCreateView,
    TaskListView,
    TaskDeleteView,
    TaskEditView,
    TaskDetailView,
    save_order,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("delete/<int:pk>", TaskDeleteView.as_view(), name="task_delete"),
    path("edit/<int:pk>", TaskEditView.as_view(), name="task_edit"),
    path("detail/<int:pk>", TaskDetailView.as_view(), name="task_detail"),
    path("save_order/", save_order, name="save_order"),
]
