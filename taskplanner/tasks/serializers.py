from rest_framework import serializers
from .models import TaskModel

class TaskShortSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TaskModel
        fields = ['id', 'title', 'description', 'deadline', 'priority', 'on_board']

class TaskSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TaskModel
        fields = ['id', 'title', 'description', 'deadline', 'priority', 'on_board', 'assignee', 'status']