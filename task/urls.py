from django.urls import path
from .apiViews import CreateTaskAPI, UpdateTaskAPI, ListTasksAPI, DeleteTaskAPI, GetTaskByIdAPI, TaskAPIView # the views are imported

app_name = 'task'
urlpatterns = [ #url list is created to contain individual url
    path('create', CreateTaskAPI.as_view(), name='create-task'),
    path('list', ListTasksAPI.as_view(), name='list-task'),
    path('update/<int:id>', UpdateTaskAPI.as_view(), name='update-task'),
    path('delete/<int:id>', DeleteTaskAPI.as_view(), name='delete-task'),
    path('detail/<int:id>', GetTaskByIdAPI.as_view(), name='task-detail'),
    path('all/<int:id>', TaskAPIView.as_view(), name='all')
    
]