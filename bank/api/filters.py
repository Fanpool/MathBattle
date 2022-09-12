from django_filters.rest_framework import FilterSet, OrderingFilter

from bank.models import Task


class TaskFilter(FilterSet):
    o = OrderingFilter(
        fields=['section', 'name']
    )

    class Meta:
        model = Task
        fields = ['section', 'name']
