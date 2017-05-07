from django import forms

from .models import Todo

class CreateForm(forms.Form):
    todo_text = forms.CharField(label='Description', max_length=160)
    todo_date = forms.CharField(label='Deadline')
    todo_progress = forms.IntegerField(label='Progress', max_value=100)

