from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from participation.models import ParticipationModel
from boards.models import BoardModel
from datetime import date

from rest_framework.exceptions import ValidationError

User = get_user_model()


class TaskModel(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    deadline = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дедлайн',
        help_text='Формат даты YYYY-MM-DD',
        validators=[MinValueValidator(
            date.today(),
            message='Дедлайн не может быть раньше сегодняшнего числа'
        )],
    )
    status = models.CharField(
        max_length=15,
        choices=[
            ('to-do', 'To-Do'),
            ('in-progress', 'Выполняется'),
            ('completed', 'Завершена')
        ],
        default='to-do',
        verbose_name='Статус'
    )
    priority = models.CharField(
        max_length=10,
        choices=[
            ('high', 'Высокий'),
            ('medium', 'Средний'),
            ('low', 'Низкий')
        ],
        verbose_name='Приоритет'
    )
    on_board = models.ForeignKey(
        BoardModel,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='На доске'
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks',
        verbose_name='Исполнитель'
    )

    def save(self, *args, **kwargs):
        if self.assignee:
            if (
                    self.assignee != self.on_board.author and
                    not ParticipationModel.objects.filter(
                        board=self.on_board, participant=self.assignee
                    ).exists()
            ):
                raise ValidationError(
                    "Можно назначить только участнику доски."
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
