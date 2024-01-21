from django.db import models


class Task(models.Model):
    """タスクモデル

    今後、以下のカラムが必要だとは思っているが、まず必要最低限を準備する。
    - タイトル
    - ステータス
    - 作成者
    - 期限
    """
    content = models.TextField("本文")
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

