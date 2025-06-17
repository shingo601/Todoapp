# todo/models.py
from django.db import models

# Create your models here. # ← この行は消してもOK

class Task(models.Model):
    # タスク名を入力するフィールド
    title = models.CharField(max_length=200, verbose_name="タスク名")

    # 完了したかどうかを表すフィールド (True/False)
    completed = models.BooleanField(default=False, verbose_name="完了フラグ")

    # タスクが作成された日時を保存するフィールド
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")

    # 管理画面などで見やすいように、タスク名を表示させる設定
    def __str__(self):
        return self.title