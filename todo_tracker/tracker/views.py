from django import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.core.urlresolvers import reverse

from .models import Todo
from .forms import CreateForm

def index(request):
   # if request.POST.get('action') == 'Delete':
    #    print("wants to delete something")
     #   t = Todo.objects.get(request.POST.get('todo_id'))
      #  t.delete()
       # return HttpResponseRedirect('/tracker/')
    latest_todo_list = Todo.objects.order_by('-todo_date')[:5]
    context = {'latest_todo_list': latest_todo_list}
       
    if(request.GET.get('mybtn')):
        Todo.objects.get(request.POST.get('todo_id')).delete()
        print("wants to delete %s" % todo.id)
        return render(request,'/tracker/')
    
    return render(request, 'tracker/index.html', context)

#def create(request):
#    if request.method == 'POST':
#        text = request.POST.get('todo_text')
#        date = request.POST.get('date')
#        progress = request.POST.get('todo_progress')
#        t = Todo(text, date, progress)
#        t.save()
#    return render(request, 'tracker/create.html')

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        print(form)
        if form.is_valid():
            print("the form is valid")
            todo_text = form.cleaned_data['todo_text']
            todo_date = form.cleaned_data['todo_date']
            todo_progress = form.cleaned_data['todo_progress']
            t = Todo(todo_text=todo_text, todo_date=todo_date, todo_progress=todo_progress)
            t.save()
            return HttpResponseRedirect('/tracker/')
        else:
            print("the form is invalid")
            return HttpResponseRedirect('/tracker/')

    else:
        print("something the form is invalid")
        form = CreateForm()
        return render(request, 'tracker/create.html', {'form': form})

def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'tracker/detail.html', {'todo': todo})

def results(request, todo_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
