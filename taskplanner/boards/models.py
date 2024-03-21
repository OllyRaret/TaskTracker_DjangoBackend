from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BoardModel(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.CharField(max_length=32)

    def __str__(self):
        return self.title