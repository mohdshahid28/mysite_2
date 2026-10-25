from django.shortcuts import render
from django.http import HttpResponse
from .models import Invoice
# Create your views here.

# create a new record
def create_onvoice(request):
    cr=Invoice.objects.create(
        cust_name = "shahid",
        invoice_num = "001",
        dis = "sardi",
        address = "ghar",
        amount = 2000,
        age = 21,
        is_paid = True,
        number = 8999999999
    )
    data = {
        'cr':cr
    }
    return render(request, 'invoices/index.html', data)
# fetch
def show_one_invoice(request):
    invoice = Invoice.objects.get(invoice_num = "001")
    data = {
        'invoice':invoice
    }
    return render(request, 'invoices/index.html', data)

# filter
def show_unpaid(request):
    unpaid_invoice = Invoice.objects.filter(is_paid = False)
    data = {
        'unpaid_invoice':unpaid_invoice
    }
    return render(request, 'invoices/index.html', data) 

def index(request):
    data ={
        'all_in':[
            {'number':1, 'name':'shahid', 'amount':3000},
            {'number':2, 'name':'arbaz', 'amount':30000},
            {'number':3, 'name':'sameer', 'amount':35000},
            {'number':4, 'name':'akhtar', 'amount':400000}
        ]
    }
    return render(request, 'invoices/index.html', data)

def contact(request):
    return render(request, 'invoices/contact.html')
def contact(request):
    return render(request, 'invoices/contact.html')
