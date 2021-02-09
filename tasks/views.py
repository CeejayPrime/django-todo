from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html')


def CreateTask(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        print("I have posted")
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/createtask.html', context)


def TodoTasks(request):
    tasks = Task.objects.all()

    # form = TaskForm()
    #
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect("/")

    context = {'tasks': tasks}
    return render(request, 'tasks/todotasks.html', context)


def UpdateTask(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form':form}
    return render(request, 'tasks/update_file.html', context)


def DeleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)


def SubTasks(request):
    subtasks = SubTask.objects.all()

    context = {'subtasks': subtasks}
    return render(request, 'subtasks/subtasks.html', context)


def CreateSubTask(request):
    subtasks = SubTask.objects.all()

    form = SubTaskForm()

    if request.method == 'POST':
        form = SubTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

        context = {'form': form, 'subtasks': subtasks}
        return render(request, 'create_subtasks.html', context)