from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    _todos = todoList.objects.all()
    return render(request, , {'todos': _todos})



#def todoCreate(request):

#def todoDelete(request):

#def todoUpdate(request):

#def todoSearch(request):