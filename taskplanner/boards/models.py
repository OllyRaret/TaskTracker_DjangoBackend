from django.db import models
from django.conf import settings


class BoardModel(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='authored_boards',
        verbose_name='Автор'
    )
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    @property
    def progress(self):
        total_tasks = self.tasks.count()
        if total_tasks == 0:
            return 0
        completed_tasks = self.tasks.filter(status='completed').count()
        return (completed_tasks / total_tasks) * 100

    class Meta:
        verbose_name = 'Доска проекта'
        verbose_name_plural = 'Доски проектов'