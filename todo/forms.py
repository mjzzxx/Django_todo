from django import forms
from .models import todoList

#To-Do list model form
class todoForm(forms.ModelForm):
    class Meta:
        model = todoList
        fields = ['title','deadline']

#검색용 form
class ListSearch(forms.Form):
    word = forms.CharField(label='검색')
