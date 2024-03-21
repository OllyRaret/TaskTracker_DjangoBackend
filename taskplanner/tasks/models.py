from django.db import models
from django.contrib.auth import get_user_model
from columns.models import ColumnModel

User = get_user_model()

class TaskModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField()
    on_column = models.ForeignKey(ColumnModel, on_delete=models.CASCADE)
    performer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title