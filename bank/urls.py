from django.urls import path
from .views import TaskListView


urlpatterns = [
    path('/tasks/<int:pk>/', TaskListView.as_view(), name='task_list'),
]
