from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('create/', views.todoCreate, name='create'),
    #path('delete/', views.todoDelete, name='delete'),
    #path('update/', views.todoUpdate, name='update'),
    #path('search', views.todoSearch, name='search')
]