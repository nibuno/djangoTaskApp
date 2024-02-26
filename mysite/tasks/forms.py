from django import forms
from .statuses import STATUS_CHOICES


class TaskSearchForm(forms.Form):
    title = forms.CharField(label="タイトル", required=False)
    content = forms.CharField(label="本文", required=False)
    status = forms.MultipleChoiceField(
        label="ステータス",
        choices=STATUS_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    limit_date = forms.DateField(
        label="期限", required=False, widget=forms.DateInput(attrs={"type": "date"})
    )
