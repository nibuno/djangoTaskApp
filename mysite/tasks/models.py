from django.contrib import auth
from django.db import models


class Task(models.Model):
    """タスクモデル

    今後、以下のカラムが必要だとは思っているが、まず必要最低限を準備する。
    - ステータス
    - 期限
    """
    title = models.CharField("タイトル", max_length=100)
    content = models.TextField("本文", blank=True)
    created_user = models.ForeignKey(
        to="auth.User",
        on_delete=models.PROTECT,
        related_name="created_user",
    )
    updated_user = models.ForeignKey(
        to="auth.User",
        on_delete=models.PROTECT,
        related_name="updated_user",
    )
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = 'task'

