from django.shortcuts import render
from django.views import generic, View
from .models import ToDoItem

# Create your views here.

class ToDoIndex(View):

    template_name = 'templates/todo/index.html'

    def get(self, request):

        context = {}
        
        if request.user.is_authenticated:
            all_ToDos = ToDoItem.objects.filter(user_name=request.user)
        
            context = {
                'all_ToDos':all_ToDos,
            }
        
        return render(request, self.template_name, context)
