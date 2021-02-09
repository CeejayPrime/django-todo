from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = '__all__'