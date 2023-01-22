from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Task


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
    tasks = Task.objects.order_by('-datecreatedtask')[:5]
    return render(request, 'task/currenttasks.html', {'tasks':tasks})

def gettasks(request):
    queryset = Task.objects.order_by('-datecreatedtask')[:5]
    return JsonResponse({"tasks":list(queryset.values())})


def viewtask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'GET':
        return render(request, 'task/viewtask.html', {'task':task,})