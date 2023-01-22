from django.contrib import admin
from .models import Task

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreatedtask',)

admin.site.register(Task, TodoAdmin)
