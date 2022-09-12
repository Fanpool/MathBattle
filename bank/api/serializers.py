from rest_framework import serializers

from bank.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['section', 'name', 'answer', 'content']
