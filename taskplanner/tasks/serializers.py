from rest_framework import serializers
from .models import TaskModel
from participation.models import ParticipationModel


class TaskShortSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TaskModel
        fields = ['id', 'title', 'description',
                  'deadline', 'priority', 'on_board']


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TaskModel
        fields = ['id', 'title', 'description',
                  'deadline', 'priority',
                  'assignee', 'status']

    def validate_assignee(self, value):
        board = self.context['view'].kwargs['board_pk']
        user = self.context['request'].user

        if not ParticipationModel.objects.filter(
                board=board,
                participant=value
        ).exists() and value != user:
            raise serializers.ValidationError(
                "Исполнитель должен быть участником доски."
            )

        return value
