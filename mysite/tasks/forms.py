from django import forms
from .statuses import STATUS_CHOICES


class TaskSearchForm(forms.Form):
    title = forms.CharField(label="タイトル", required=False)
    content = forms.CharField(label="本文", required=False)
    # FIXME: 初期画面遷移時にフィルタリングしている状況と合わない気がするのでレイアウト踏まえて修正検討
    status = forms.ChoiceField(
        label="ステータス",
        choices=[("", "---------")] + list(STATUS_CHOICES),
        required=False,
    )
