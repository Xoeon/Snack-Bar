from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Snack(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='snack/images/')
    url = models.URLField(max_length=500)
    description = models.CharField('DESCRIPTION', max_length=300, blank=True)
    is_accepted = models.BooleanField('IS_ACCEPTED', default=False)
    supply_year = models.PositiveSmallIntegerField(
        'SUPPLY_YEAR', default=2023, null=True)
    supply_month = models.PositiveSmallIntegerField(
        'SUPPLY_MONTH', null=True,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1),
        ]
    )
    create_date = models.DateTimeField(default=timezone.now)
    requester = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name='requester_snack')
    voter = models.ManyToManyField(User, related_name='voter_snack')

    def __str__(self):
        return self.name
