from django import forms
from .models import ToDoItem

class ToDoItemForm(form.ModelForm):

    class Meta:
        model = ToDoItem
        fields = [
            'content',
        ]
