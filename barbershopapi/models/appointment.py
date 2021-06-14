from django.db import models


class Appointment(models.Model):

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    barber = models.ForeignKey("Barber", on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    services = models.ForeignKey("Service", on_delete=models.CASCADE)

