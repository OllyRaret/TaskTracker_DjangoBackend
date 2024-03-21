from django.db import models
from django.contrib.auth import get_user_model
from boards.models import BoardModel

User = get_user_model()

class ParticipationModel(models.Model):
    participant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='participant'
    )
    board = models.ForeignKey(
        BoardModel,
        on_delete=models.CASCADE,
        related_name='board_in_work'
    )
    can_edit = models.BooleanField()

    def __str__(self):
        return f'{self.participant} participates in {self.board}'