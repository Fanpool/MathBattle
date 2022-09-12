from django.contrib import admin
from .models import Task, Section


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
