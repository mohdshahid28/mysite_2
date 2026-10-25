from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('show_one_invoice', views.show_one_invoice, name='show_one_invoice'),
    path('create_onvoice', views.create_onvoice, name='create_onvoice'),

]
