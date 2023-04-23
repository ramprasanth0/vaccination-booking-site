from django.db import models

# Create your models here.

class vaccination_centre(models.Model):
    name=models.CharField(max_length=200)
    working_hours=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    slots_per_day=models.CharField(max_length=200)
    ucontact=models.CharField(max_length=10)

    def __str__(self):
        return self.name
