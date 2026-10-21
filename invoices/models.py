from django.db import models

# Create your models here.
class Invoice(models.Model):
    cust_name = models.CharField(max_length=500),
    invoice_num = models.CharField(max_length=50),
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.invoice_num - self.cust_name
   