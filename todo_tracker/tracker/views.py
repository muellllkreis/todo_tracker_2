from django import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.core.urlresolvers import reverse

from .models import Todo
from .forms import CreateForm
from .forms import DeleteForm

def index(request):
    latest_todo_list = Todo.objects.order_by('-todo_date')[:5]
    context = {'latest_todo_list': latest_todo_list} 
    return render(request, 'tracker/index.html', context)

def delete(request, todo_id):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        Todo.objects.get(id=todo_id).delete()
        return HttpResponseRedirect('/tracker/')

    else:
        form = DeleteForm()
        return render(request, 'tracker/create.html', {'form': form})

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            todo_text = form.cleaned_data['todo_text']
            todo_date = form.cleaned_data['todo_date']
            todo_progress = form.cleaned_data['todo_progress']
            t = Todo(todo_text=todo_text, todo_date=todo_date, todo_progress=todo_progress)
            t.save()
            return HttpResponseRedirect('/tracker/')
        else:
            return HttpResponseRedirect('/tracker/')

    else:
        form = CreateForm()
        return render(request, 'tracker/create.html', {'form': form})

def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    #todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'tracker/edit.html', {'todo': todo})

def results(request, todo_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
