from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

def todo_list(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo_app/list.html', context=context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(request, 'todo_app/update_task.html', context=context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("/")

    context = {'item': item}
    return render(request, 'todo_app/delete.html', context=context)
