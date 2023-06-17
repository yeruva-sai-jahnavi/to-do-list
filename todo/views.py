# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("working")

# class base views
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'task'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'
