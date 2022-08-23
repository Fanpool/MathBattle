from ckeditor.fields import RichTextField
from django.db import models


class Section(models.Model):
    name = models.CharField(verbose_name='Name', max_length=120)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return self.name


class Task(models.Model):
    section = models.ForeignKey('bank.Section', on_delete=models.SET_NULL, verbose_name='Section', null=True)
    name = models.CharField(max_length=120, verbose_name='Название')
    answer = models.CharField(max_length=255, verbose_name='Answer')
    content = RichTextField()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return '[%s] %s' % (self.section, self.name)
