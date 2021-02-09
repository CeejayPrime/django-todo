from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('update_file/<str:pk>/', views.UpdateTask, name="UpdateTask"),
    path('delete/<str:pk>/', views.DeleteTask, name="delete"),
    path('createtask/', views.CreateTask, name="CreateTask"),
    path('todotasks/', views.TodoTasks, name="TodoTasks"),
    path('subtasks/', views.SubTasks, name="SubTasks"),
    path('create_subtasks/', views.CreateSubTask, name="CreateSubTask")
]
