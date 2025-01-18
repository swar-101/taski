from django.urls import path

from tasks.views import TaskViewSet

urlPatterns = [
 path('tasks/', TaskViewSet.as_view(), name = 'task-list')
]