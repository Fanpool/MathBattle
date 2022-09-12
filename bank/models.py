from django.db import models
from django_quill.fields import QuillField


class Section(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=120)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return self.name


class Task(models.Model):
    section = models.ForeignKey('bank.Section', on_delete=models.SET_NULL, verbose_name='Раздел', null=True)
    name = models.CharField(max_length=120, verbose_name='Название')
    answer = models.CharField(max_length=255, verbose_name='Ответ')
    content = QuillField()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return '[%s] %s' % (self.section, self.name)
