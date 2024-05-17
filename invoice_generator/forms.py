from django import forms
from .models import Invoice, Client

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number','customer', 'created_at', 'due_date', 'paid', 'total']

        model = Client
        fields = ['name', 'email', 'address', 'company_name']