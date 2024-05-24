from django.urls import path
from .views import generate_invoice_pdf, view_invoice, edit_invoice, delete_invoice
from . import views

app_name = 'invoice_generator'

urlpatterns = [
    path('create/',views.create_invoice, name='create_invoice'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('home/', views.home, name='home'),
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('invoice/<int:invoice_id>/pdf/', generate_invoice_pdf, name='generate_invoice_pdf'),
    path('invoice/<int:invoice_id>/', view_invoice, name='view_invoice'),
    path('invoice/<int:invoice_id>/edit/', edit_invoice, name='edit_invoice'),
    path('invoice/<int:invoice_id>/delete/', delete_invoice, name='delete_invoice'),
]