from django.urls import path
from .views import ToDoIndex

urlpatterns = [
   path('', ToDoIndex.as_view(), name='index')
]
