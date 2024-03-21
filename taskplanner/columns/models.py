from django.db import models
from boards.models import BoardModel

class ColumnModel(models.Model):
    title = models.CharField(max_length=64)
    priority = models.PositiveSmallIntegerField()
    on_board = models.ForeignKey(
        BoardModel,
        on_delete=models.CASCADE,
        related_name='on_board'
    )

    def __str__(self):
        return self.title