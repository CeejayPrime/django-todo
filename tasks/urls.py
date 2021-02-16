from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.RegisterPage, name="RegisterPage"),
    path('login/', views.LoginPage, name="LoginPage"),
    path('logout/', views.LogoutUser, name="LogoutUser"),
    path('update_file/<str:pk>/', views.UpdateTask, name="UpdateTask"),
    path('delete/<str:pk>/', views.DeleteTask, name="delete"),
    path('createtask/', views.CreateTask, name="CreateTask"),
    path('todotasks/', views.TodoTasks, name="TodoTasks"),
    path('subtasks/', views.SubTasks, name="SubTasks"),
    path('create_subtasks/', views.CreateSubTask, name="CreateSubTask"),
    path('update_subtask/<str:pk>/', views.UpdateSubTask, name="UpdateSubTask"),
    path('delete_subtask/<str:pk>/', views.DeleteSubTask, name="DeleteSubTask"),
]
