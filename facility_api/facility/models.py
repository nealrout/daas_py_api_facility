from django.db import models

class Facility(models.Model):
    fac_code = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    create_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

