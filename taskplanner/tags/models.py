from django.db import models

class TagModel(models.Model):
    name = models.CharField(max_length=64)
    color_code = models.CharField(max_length=8)
    slug = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name