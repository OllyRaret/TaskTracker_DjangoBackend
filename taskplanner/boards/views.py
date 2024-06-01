from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import BoardModel
from .serializers import BoardSerializer

class DashboardView(generics.ListAPIView):
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return BoardModel.objects.filter(
            Q(author=user) | Q(board_in_work__participant=user)
        ).distinct()
