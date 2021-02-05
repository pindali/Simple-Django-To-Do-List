from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    constext = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', constext)


def updateTask(request, pk):
    tasks = task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = task.objects.get(id=pk)
    context = {'item' : item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'tasks/delete.html', context)
    

    
