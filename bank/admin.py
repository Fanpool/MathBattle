from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms

from .models import Task, Section


class TaskAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Task
        fields = ('section', 'name', 'content', 'answer')


class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm


class SectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
admin.site.register(Section, SectionAdmin)
