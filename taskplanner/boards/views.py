from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import BoardModel
from .serializers import BoardSerializer


class DashboardView(ModelViewSet):
    queryset = BoardModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BoardSerializer
    http_method_names = ['get', 'post', 'patch', 'create', 'delete']

    def get_queryset(self):
        user = self.request.user
        return BoardModel.objects.filter(
            Q(author=user) | Q(board_in_work__participant=user)
        ).distinct()
