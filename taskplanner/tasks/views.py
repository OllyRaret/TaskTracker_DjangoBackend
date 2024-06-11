from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import TaskModel
from .serializers import TaskSerializer, TaskShortSerializer


class TaskListView(ModelViewSet):
    queryset = TaskModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskShortSerializer

    def get_queryset(self):
        user = self.request.user
        return TaskModel.objects.filter(
            Q(assignee=user)
        ).exclude(status='completed').distinct()

class TaskCalendarView(ModelViewSet):
    queryset = TaskModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return TaskModel.objects.filter(
            Q(assignee=user)
        ).distinct()

class TaskViewSet(ModelViewSet):
    queryset = TaskModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        board_id = self.kwargs['board_pk']
        return TaskModel.objects.filter(on_board__id=board_id)

    def perform_create(self, serializer):
        board_id = self.kwargs['board_pk']
        serializer.save(on_board_id=board_id)