from django.db import models
from django.contrib.auth import get_user_model
from boards.models import BoardModel

User = get_user_model()

class ParticipationModel(models.Model):
    participant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='participant',
        verbose_name='Участник'
    )
    board = models.ForeignKey(
        BoardModel,
        on_delete=models.CASCADE,
        related_name='board_in_work',
        verbose_name='Доска проекта'
    )
    can_edit = models.BooleanField(verbose_name='Права на редактирование')

    def __str__(self):
        return f'{self.participant} участвует в проекте {self.board}' + (' как администратор' if self.can_edit else '')

    class Meta:
        verbose_name = 'Участие в проекте'
        verbose_name_plural = 'Участия в проектах'

        constraints = [
            models.UniqueConstraint(
                fields=['participant', 'board'],
                name='Уникальность участия в проекте',
                violation_error_message='Этот пользователь уже участвует в проекте'
            )
        ]
