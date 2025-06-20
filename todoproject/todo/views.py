from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
# forms.py から TaskForm をインポートします
from .forms import TaskForm

# タスク一覧ビュー (これは既存のコード)
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# ↓↓ ここから下を追記 ↓↓

# タスク作成ビュー
def task_create(request):
    # もしリクエストが「POST」の場合 (＝フォームが送信された場合)
    if request.method == 'POST':
        # 送信されたデータ (request.POST) を元にフォームを作成
        form = TaskForm(request.POST)
        # フォームの入力内容が正しいかチェック
        if form.is_valid():
            # 正しければ、データベースに保存
            form.save()
            # タスク一覧ページに移動 (リダイレクト)
            return redirect('task_list')
    # もしリクエストが「GET」の場合 (＝通常のページアクセス)
    else:
        # 空のフォームを作成
        form = TaskForm()
    
    
    return render(request, 'todo/task_form.html', {'form': form})

def task_update(request, pk):
    
    
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:

        form = TaskForm(instance=task)

    return render(request, 'todo/task_form.html', {'form': form, 'task': task})

# タスク削除ビュー
def task_delete(request, pk):
    #削除対象のタスクを習得
    task = get_object_or_404(Task, pk=pk)

    #もしリクエストがPOSTなら（削除ボタンがおされたら）
    if request.method == 'POST':
        #タスクを削除
        task.delete()
        #タスク一覧ページにリダイレクト
        return redirect('task_list')
    
    #POSTでない場合は、削除確認ページを表示
    return render(request, 'todo/task_confirm_delete.html', {'task': task})
