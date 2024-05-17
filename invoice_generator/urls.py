from django.urls import path
from .views import generate_invoice_pdf,invoice, dashboard

app_name = 'invoice_generator'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('invoice/', invoice, name='invoice'),
    path('invoice/<int:invoice_id>/pdf/', generate_invoice_pdf, name='generate_pdf_invoice'),
]