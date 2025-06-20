# todo/forms.py
from django import forms
from .models import Task # models.pyからTaskモデルをインポート

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # このフォームは「Task」モデルと連携します
        fields = ['title', 'completed'] # フォームには「title」と「completed」の入力欄を表示します