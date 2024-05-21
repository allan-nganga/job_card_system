from django.urls import path
from .views import generate_invoice_pdf
from . import views

app_name = 'invoice_generator'

urlpatterns = [
    path('create/',views.create_invoice, name='create_invoice'),
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('invoice/<int:invoice_id>/pdf/', generate_invoice_pdf, name='generate_pdf_invoice'),
]