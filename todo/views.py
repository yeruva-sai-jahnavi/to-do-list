# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("working")

# class base views
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'task'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'  # all the fields in models.Task
    success_url = reverse_lazy('task')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task')
