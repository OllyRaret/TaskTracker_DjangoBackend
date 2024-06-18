from django.db.models import Q, Case, When, Value, IntegerField
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from boards.models import BoardModel
from participation.models import ParticipationModel
from .models import TaskModel
from .serializers import TaskSerializer
from .serializers import TaskShortSerializer


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
        return (
            TaskModel.objects
            .filter(on_board__id=board_id)
            .annotate(
                priority_order=Case(
                    When(priority='high', then=Value(1)),
                    When(priority='medium', then=Value(2)),
                    When(priority='low', then=Value(3)),
                    output_field=IntegerField(),
                )
            )
            .order_by('priority_order')
        )

    def perform_create(self, serializer):
        board = get_object_or_404(BoardModel, pk=self.kwargs['board_pk'])
        user = self.request.user
        if not ParticipationModel.objects.filter(
                board=board,
                participant=user
        ).exists():
            raise PermissionDenied(
                "Вы не являетесь участником данного проекта."
            )
        serializer.save(on_board=board)

    def perform_update(self, serializer):
        board = get_object_or_404(BoardModel, pk=self.kwargs['board_pk'])
        user = self.request.user
        if not ParticipationModel.objects.filter(
                board=board,
                participant=user
        ).exists():
            raise PermissionDenied(
                "Вы не являетесь участником данного проекта."
            )
        serializer.save(on_board=board)
