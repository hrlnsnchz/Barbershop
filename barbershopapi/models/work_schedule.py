from django.db import models
from django.utils.timezone import now

class Work_Schedule(models.Model):

    barber = models.ForeignKey("Barber", on_delete=models.CASCADE)
    working_from = models.DateTimeField(default=now)
    working_to = models.DateTimeField(default=now)