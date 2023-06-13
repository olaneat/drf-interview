from django.urls import path
from .apiViews import CreateTaskAPI, UpdateTaskAPI, ListTasksAPI, DeleteTaskAPI

app_name = 'task'
urlpatterns = [
    path('create', CreateTaskAPI.as_view(), name='create-task'),
    path('list', ListTasksAPI.as_view(), name='list-task'),
    path('update/<int:id>', UpdateTaskAPI.as_view(), name='update-task'),
    path('delete/<int:id>', DeleteTaskAPI.as_view(), name='delete-task')
    
]