from django.db import models

class Waitlist_Service(models.Model):

    waitlist = models.ForeignKey("Waitlist", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)