from boards.models import BoardModel
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import ParticipationModel
from .models import UserModel
from .serializers import ParticipationSerializer, AddParticipantSerializer
from .serializers import UserSerializer, MyTokenObtainPairSerializer, ProfileSerializer


class RegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class TeamViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, project_pk=None):
        board = BoardModel.objects.get(pk=project_pk)
        participants = ParticipationModel.objects.filter(board=board)
        serializer = ParticipationSerializer(participants, many=True)
        return Response(serializer.data)

    def create(self, request, project_pk=None):
        board = get_object_or_404(BoardModel, pk=project_pk)
        serializer = AddParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(board=board)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, project_pk=None):
        board = get_object_or_404(BoardModel, pk=project_pk)
        participation = get_object_or_404(ParticipationModel, pk=pk, board=board)
        participation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None, project_pk=None):
        board = get_object_or_404(BoardModel, pk=project_pk)
        participation = get_object_or_404(ParticipationModel, pk=pk, board=board)
        participation.can_edit = True
        participation.save()
        serializer = ParticipationSerializer(participation)
        return Response(serializer.data)

class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

    def partial_update(self, request):
        serializer = ProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)