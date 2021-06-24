from django.db import models
from django.utils.timezone import now

class Appointment(models.Model):

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    barber = models.ForeignKey("Barber", on_delete=models.CASCADE)
    start = models.DateTimeField(default=now)
    end = models.DateTimeField(default=now)
    services = models.ManyToManyField("Service")

