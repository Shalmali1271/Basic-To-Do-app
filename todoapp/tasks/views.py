from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.



def updateTask(request, pk) : 
    task = Task.objects.get(id=pk)
    form = TaskForm(instance = task)

    if request.method == "POST" :
        form = TaskForm(request.POST, instance = task)
        if form.is_valid() :
            form.save()
        return redirect('/')
    context = {'form' : form}
    return render(request, 'tasks/Update_task.html', context)

def deleteTask(request, pk) :
    item = Task.objects.get(id=pk)
    if request.method == "POST" :
        item.delete()
        return redirect('/')
    context = {'item' : item}
    return render(request, 'tasks/delete.html', context)

def index(request) : 
    
    tasks = Task.objects.all()
    form = TaskForm()

    context = {'tasks' : tasks, 'form' : form}

   
    if request.method == 'POST' :
        form = TaskForm(request.POST)
        if form.is_valid() :
            user = request.user
            form.save()
        return redirect('/')

    return render(request, 'tasks/list.html', context)