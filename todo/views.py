from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView
from django.db.models import Q
from .models import todoList
from .forms import todoForm, ListSearch

# Create your views here.

# 사이트 메인 화면
def index(request):
    _todos = todoList.objects.all()
    return render(request, 'index.html', {'todos': _todos})

# 리스트 작성
def todoCreate(request):
    form = todoForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid(): #form의 값이 올바른지 확인
            todoList = form.save(commit=False) #form 저장
            todoList.save()
            return redirect('/')
        else:
            form = todoForm()
    return render(request, 'Create.html',{'form': form})

#리스트 삭제
def todoDelete(request, todo_id):
    todo = todoList.objects.get(id = todo_id) #대상 객체 지정
    todo.delete() #form 삭제
    return redirect('/')

#리스트 수정
def todoUpdate(request, todo_id):
    todo = todoList.objects.get(id = todo_id) #대상 객체 지정
    form = todoForm(request.POST, instance=todo)
    if form.is_valid(): #form의 값이 올바른지 확인
        todo = form.save(commit=False) #form 저장   
        todo.save()
        return redirect('/')
    else:
        form = todoForm(instance=todo)
    return render(request, 'Update.html',{'form': form})

#리스트 검색
class todoSearch(FormView):
    form_class = ListSearch
    template_name = 'Search.html'

    def form_valid(self, form): #form의 값이 올바른지 확인
        Word = form.cleaned_data['word']
       
        #filter 적용 : title에 입력된 문자가 존재하는지
        List = todoList.objects.filter(
            Q(title__icontains = Word)
        ).distinct()
        
        #검색 결과
        context = {
            'form': form, 'Search': Word, 'List': List
        }
        return render(self.request, self.template_name, context)
