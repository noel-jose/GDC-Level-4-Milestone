from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

tasks = []
completed = []


def task_view(request):
    return render(request, "task.html", {"tasks": tasks})


def add_task_view(request):
    task = request.GET.get("task")
    tasks.append(task)
    return HttpResponseRedirect("/tasks/")


def delete_task_view(request, index):
    tasks.pop(index - 1)
    return HttpResponseRedirect("/tasks/")


def complete_task_view(request, index):
    completed_task = tasks.pop(index - 1)
    completed.append(completed_task)
    return HttpResponseRedirect("/tasks/")


def completed_task_view(request):
    return render(request, "completed.html", {"tasks": completed})


def all_tasks_view(request):
    return render(request, "all.html", {"tasks": tasks, "completed": completed})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", task_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    path("complete_task/<int:index>/", complete_task_view),
    path("completed_tasks/", completed_task_view),
    path("all_tasks/", all_tasks_view),
]
