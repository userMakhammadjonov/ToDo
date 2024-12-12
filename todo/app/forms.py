from django import forms
from .models import Task,List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['user','name']
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['list','name']
