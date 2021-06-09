from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.todoCreate, name='todoCreate'),
    path('delete/<int:todo_id>/', views.todoDelete, name='todoDelete'),
    path('update/<int:todo_id>/', views.todoUpdate, name='todoUpdate'),
    path('search/', views.todoSearch.as_view(), name='search')
]