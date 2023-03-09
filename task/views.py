from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm


def home(request):
    return render(request, 'task/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'task/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttasks')
            except IntegrityError:
                return render(request, 'task/signupuser.html', {'form':UserCreationForm(), 'error':'This name is already taken! Choose another name.'})
        else:
            return render(request, 'task/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match!'})

def currenttasks(request):
    if request.user.is_superuser:
        arrayLen = len(Task.objects.all())
        print(arrayLen)
        return render(request, 'task/currenttasks.html', {'len': arrayLen})
    else:
        arrayLen = len(Task.objects.filter(user=request.user))
        print(arrayLen)
        return render(request, 'task/currenttasks.html', {'len': arrayLen})

def gettasks(request, **kwargs):
    if request.user.is_superuser:
        print(request.user)
        upper = kwargs.get ('num_posts')
        lower = upper - 3
        Posts = list(Task.objects.values()[lower:upper])
        return JsonResponse({'data': Posts},  safe=False)
    else:
        print(request.user)
        upper = kwargs.get ('num_posts')
        lower = upper - 3
        Posts = list(Task.objects.filter(user=request.user).values()[lower:upper])
        return JsonResponse({'data': Posts},  safe=False)

def getNewTask(request, **kwargs):
    if request.user.is_superuser:
        lastPost = kwargs.get ('new_task')
        queryset = list(Task.objects.values()[lastPost:])
        return JsonResponse({"newTask":queryset}, safe=False)
    else:
        lastPost = kwargs.get ('new_task')
        queryset = list(Task.objects.filter(user=request.user).values()[lastPost:])
        return JsonResponse({"newTask":queryset}, safe=False)

def viewtask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'GET':
        return render(request, 'task/viewtask.html', {'task':task})
    
def createtasks(request):
    if request.method == 'GET':
        return render(request, 'task/createtask.html', {'form':TaskForm()})
    else:    
        try:
            form = TaskForm(request.POST)
            newtask = form.save(commit=False)
            newtask.user = request.user
            newtask.username = request.user
            newtask.save()
            return redirect('currenttasks')
        except ValueError:
            return render(request, 'task/createtask.html', {'form':TaskForm(), 'error':'bad value'})
        
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'task/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'task/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password not match!'})
        else:
            login(request, user)
            return redirect('currenttasks')