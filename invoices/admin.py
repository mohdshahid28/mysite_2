from django.contrib import admin
from .models import Invoice
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        'cust_name', 'invoice_num','amount','is_paid','date'
    ]
    search_fields=['cust_name', 'invoice_num']
    list_filter= ['is_paid','date']
    ordering=['date']


admin.site.register(Invoice,InvoiceAdmin)