from django.contrib import admin
from .models import Tasks, TaskList
# Register your models here.

admin.site.register(TaskList)
admin.site.register(Tasks)
