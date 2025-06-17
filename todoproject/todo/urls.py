# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ここに、これからURLのルールをどんどん追加していきます
    path('', views.task_list, name='task_list'),

]