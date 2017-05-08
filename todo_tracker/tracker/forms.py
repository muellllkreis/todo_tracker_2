from django import forms

from .models import Todo

class CreateForm(forms.Form):
    todo_text = forms.CharField(max_length=160,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5',
                'placeholder': 'Description (less than 160 chars)',
            }))
    todo_date = forms.DateField(widget = forms.SelectDateWidget(attrs={'class': 'form-control',}))
    todo_progress = forms.IntegerField(label='Progress', max_value=100, min_value=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '80',
            }))

class DeleteForm(forms.Form):
    todo_id = forms.CharField(max_length=0)

class EditForm(forms.Form):
    todo_text = forms.CharField(max_length=160,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5',
                'placeholder': 'Description (less than 160 chars)',
            }))
    todo_date = forms.DateField(widget = forms.SelectDateWidget(attrs={'class': 'form-control',}))
    todo_progress = forms.IntegerField(label='Progress', max_value=100, min_value=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '80',
            }))

