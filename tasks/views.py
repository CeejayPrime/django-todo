from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Successfully Created for ' + user)
                return redirect('LoginPage')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html')


def LogoutUser(request):
    logout(request)
    return redirect('LoginPage')


@login_required(login_url='LoginPage')
def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html')


def UserPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='LoginPage')
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


@login_required(login_url='LoginPage')
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
    context = {'form': form}
    return render(request, 'tasks/update_file.html', context)


@login_required(login_url='LoginPage')
def DeleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)


@login_required(login_url='LoginPage')
def SubTasks(request):
    subtasks = SubTask.objects.all()

    contexts = {'subtasks': subtasks}
    return render(request, 'subtasks/subtasks.html', contexts)


@login_required(login_url='LoginPage')
def CreateSubTask(request):
    subtasks = SubTask.objects.all()

    form = SubTaskForm()

    if request.method == 'POST':
        form = SubTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form, 'subtasks': subtasks}
    return render(request, 'subtasks/create_subtasks.html', context)


@login_required(login_url='LoginPage')
def UpdateSubTask(request, pk):
    subtasks = SubTask.objects.get(id=pk)
    form = SubTaskForm(instance=subtasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=subtasks)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(request, 'subtasks/update_subtask.html', context)


@login_required(login_url='LoginPage')
def DeleteSubTask(request, pk):
    item = SubTask.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'subtasks/delete_subtask.html', context)