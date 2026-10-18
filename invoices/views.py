from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
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