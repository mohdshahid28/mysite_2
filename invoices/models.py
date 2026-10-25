from django.db import models
from django.utils import timezone
# Create your models here.

class Invoice(models.Model):
    cust_name = models.CharField(max_length=500,default="")
    invoice_num = models.CharField(max_length=50, default="")
    dis = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=500, default="")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    age = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return self.cust_name
   