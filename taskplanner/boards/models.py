from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BoardModel(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.CharField(max_length=32)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    deadline = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title