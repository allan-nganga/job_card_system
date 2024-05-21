from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'client_name',
            'company_name',
            'billing_address',
            'item_description',
            'item_quantity',
            'item_price',  
            'due_date', 
            'paid'
        ]

"""
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name', 
            'email', 
            'address', 
            'company_name'
            ]
            """