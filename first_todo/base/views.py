from django.shortcuts import render, redirect

from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'base/index.html', context=context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'task': task, 'form': form}

    return render(request, 'base/update_task.html', context=context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}

    return render(request, 'base/delete_task.html', context=context)