from django.db import models
from reservation.models import Table

# Create your models here.
class Waitlist(models.Model):
    
    id = models.IntegerField(primary_key=True)
    guests = models.IntegerField()
    lastname = models.CharField(max_length=128)
    catagory = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'waitlist'
        verbose_name_plural = 'waitlist'