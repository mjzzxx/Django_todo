from django.db import models

# Create your models here.

#To-Do list model
class todoList(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    deadline = models.DateField(verbose_name="날짜")

    def __str__(self):
        return self.title