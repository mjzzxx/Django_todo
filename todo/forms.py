from django import forms
from .models import todoList

class todoForm(forms.ModelForm):
    class Meta:
        model = todoList
        fields = ['title','deadline']

class ListSearch(forms.Form):
    word = forms.CharField(label='검색')
