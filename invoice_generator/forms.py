from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'pub_date', 'due_date', 'client_name', 'client_email', 'company_name', 'company_address']