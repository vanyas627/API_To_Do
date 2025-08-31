from django.urls import path
from .views import TaskListCreateView, TaskDetailView, RegisterView
urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('register/', RegisterView.as_view(), name='register'),

]