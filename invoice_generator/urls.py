from django.urls import path
from .views import generate_invoice_pdf,invoice

urlpatterns = [
    path('invoice/', invoice, name='invoice'),
    path('invoice/<int:invoice_id>/pdf/', generate_invoice_pdf, name='generate_pdf_invoice'),
]