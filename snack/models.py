from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Snack(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='snack/images/')
    url = models.URLField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now)
    requester = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.name
