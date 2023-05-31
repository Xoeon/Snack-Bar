from django.db import models


class Snack(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    url = models.URLField(max_length=500)
