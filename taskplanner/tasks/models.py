from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from boards.models import BoardModel
from datetime import date

User = get_user_model()

class TaskModel(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
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
        choices=[('to-do', 'To-Do'), ('in-progress', 'Выполняется'), ('completed', 'Завершена')],
        default='to-do',
        verbose_name='Статус'
    )
    priority = models.CharField(
        max_length=10,
        choices=[('high', 'Высокий'), ('medium', 'Средний'), ('low', 'Низкий')],
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
        verbose_name='Исполнитель'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
