from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Invoice
from .forms import InvoiceForm
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
    all_in=Invoice.objects.all()
    data ={
        'all_in':all_in
        
    }
    return render(request, 'invoices/index.html', data)


def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InvoiceForm()

    data = {
        'form':form
    }
    
    return render(request, 'invoices/add_invoice.html',data)



def contact(request):
    return render(request, 'invoices/contact.html')
def contact(request):
    return render(request, 'invoices/contact.html')
