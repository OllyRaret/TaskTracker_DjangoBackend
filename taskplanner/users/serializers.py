from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from participation.models import ParticipationModel
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    @atomic
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token


class ParticipationSerializer(serializers.ModelSerializer):
    participant = UserSerializer()

    class Meta:
        model = ParticipationModel
        fields = ['id', 'participant', 'board', 'can_edit']


class AddParticipantSerializer(serializers.ModelSerializer):
    participant_id = serializers.IntegerField()

    class Meta:
        model = ParticipationModel
        fields = ['participant_id', 'board', 'can_edit']

    @atomic
    def create(self, validated_data):
        participant_id = validated_data.pop('participant_id')
        participant = get_user_model().objects.get(id=participant_id)
        participation = ParticipationModel.objects.create(
            participant=participant,
            **validated_data
        )
        return participation


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
