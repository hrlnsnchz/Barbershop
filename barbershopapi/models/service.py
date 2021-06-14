from django.db import models

class Service(models.Model):

    label = models.CharField(max_length=100, default="")
    price = models.FloatField(default=0.00)
