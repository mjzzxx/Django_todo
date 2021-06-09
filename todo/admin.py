from django.contrib import admin

# Register your models here.
from .models import todoList

admin.site.register(todoList)