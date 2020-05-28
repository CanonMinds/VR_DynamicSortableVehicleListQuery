from django.db import models

import uuid
from django.urls import reverse

# Create your models here.

class Car(models.Model):
    REDCAR = 'Red Car'
    BLUECAR = 'Blue Car'
    GREENCAR = 'Green Car'
    CAR_COLOR_CHOICES = [
        (REDCAR, 'RedCar'),
        (BLUECAR, 'BlueCar'),
        (GREENCAR,'Green Car'),
    ]
    name = models.CharField(
        max_length=200,
        choices=CAR_COLOR_CHOICES,
        default=REDCAR,)
    lookup_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    order = models.IntegerField(blank=False, default=100_000)
    description = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_edit', kwargs={'pk': self.pk})