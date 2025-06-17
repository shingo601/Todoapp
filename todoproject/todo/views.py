from django.shortcuts import render
from .models import Task
# Create your views here.

#タスク一覧を表示するためのビュー
def task_list(request):
    #データベースからすべてのタスクを習得する
    tasks = Task.objects.all().order_by('created_at')

    # 取得したタスクのデータをテンプレートに渡して、HTMLを生成する
    # この時点では 'todo/task_list.html' はまだ存在しません
    return render(request, 'todo/task_list.html', {'tasks': tasks})