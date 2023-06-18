from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskListView.as_view(), name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
]
