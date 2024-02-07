from django.contrib import auth
from django.db import models

from .statuses import STATUS_CHOICES


class Task(models.Model):
    """タスクモデル"""

    title = models.CharField("タイトル", max_length=100)
    content = models.TextField("本文", blank=True)
    status = models.IntegerField(
        verbose_name="ステータス", choices=STATUS_CHOICES, default=0
    )
    created_user = models.ForeignKey(
        to="auth.User",
        on_delete=models.PROTECT,
        related_name="created_user",
    )
    limit_date = models.DateField(verbose_name="期限", blank=True, null=True)
    updated_user = models.ForeignKey(
        to="auth.User",
        on_delete=models.PROTECT,
        related_name="updated_user",
    )
    created_at = models.DateTimeField(verbose_name="投稿日", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日", auto_now=True)

    class Meta:
        db_table = "task"
