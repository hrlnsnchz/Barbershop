from django.db import models



class Customer(models.Model):

    name = models.CharField(max_length=70)
    phone = models.IntegerField()