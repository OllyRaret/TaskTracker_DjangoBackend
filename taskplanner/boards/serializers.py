from django.db.transaction import atomic
from rest_framework import serializers
from .models import BoardModel

class BoardSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = BoardModel
        fields = ['id', 'title', 'progress', 'deadline', 'priority']

    @atomic
    def create(self, validated_data):
        user = self.context['request'].user
        return BoardModel.objects.create(author=user, **validated_data)

    @atomic
    def update(self, instance: BoardModel, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

