from django.db import models
from django.utils import timezone


class Snack(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    url = models.URLField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
