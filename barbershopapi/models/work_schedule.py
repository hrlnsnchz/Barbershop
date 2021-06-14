from django.db import models

class Work_Schedule(models.Model):

    barber = models.ForeignKey("Barber", on_delete=models.CASCADE)
    datetime = models.DateTimeField()