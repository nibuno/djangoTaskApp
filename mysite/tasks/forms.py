from django import forms


class TaskSearchForm(forms.Form):
    title = forms.CharField(label="タイトル", required=False)
