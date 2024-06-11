from django.db.transaction import atomic
from rest_framework import serializers
from .models import BoardModel
from participation.models import ParticipationModel

class BoardSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = BoardModel
        fields = ['id', 'title', 'progress']

    @atomic
    def create(self, validated_data):
        user = self.context['request'].user
        board = BoardModel.objects.create(author=user, **validated_data)
        ParticipationModel.objects.create(participant=user, can_edit=True, board_id=board.id)
        return board

    @atomic
    def update(self, instance: BoardModel, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

