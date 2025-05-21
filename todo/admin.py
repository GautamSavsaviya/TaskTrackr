from django.contrib import admin
from django.contrib.admin import ModelAdmin
from todo.models import Todo


# Register your models here.
class TodoAdmin(ModelAdmin):
    list_display = ["title", "status", "due_date"]


admin.site.register(Todo, TodoAdmin)
