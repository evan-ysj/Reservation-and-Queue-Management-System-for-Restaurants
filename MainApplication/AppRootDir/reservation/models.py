from django.db import models

# Create your models here.
class Table(models.Model):
    
    table_id = models.AutoField(primary_key=True)
    cap = models.IntegerField(default=4)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return str(self.table_id)

    class Meta:
        verbose_name = 'table'
        verbose_name_plural = 'table'


class Reservation(models.Model):

    rsv_number = models.AutoField(primary_key=True)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    no_of_guests = models.IntegerField(default=4)
    user = models.CharField(max_length=128)
    date = models.DateField()
    rsv_time = models.DateTimeField(auto_now_add=True)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return str(self.rsv_number)

    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservation' 


