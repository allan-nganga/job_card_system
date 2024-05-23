from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import Invoice
from .forms import InvoiceForm

# Create your views here.
def invoice(request):
    return render(request, 'invoice_template.html', {})

def generate_invoice_pdf(request, id):
    # Retrieve the invoice object
    invoice = Invoice.objects.get(id=id)

    # Render the HTML template with invoice data
    # template = get_template('invoice/invoice_template.html')
    html_string = render_to_string('Invoice/invoice_template.html', {'invoice': invoice})

    # Create a PDF file using WeasyPrint
    pdf_file = HTML(string=html_string).write_pdf()

    # Create a HTTP response with PDF as content type
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=invoice_{invoice.id}.pdf'
    return response

# invoice generate function
def create_invoice(request):
    context = {'page_title':'Create Invoice'}
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('invoice_generator:invoice_detail', invoice_id=invoice.id)
        else:
            return render(request, 'invoice/create_invoice.html', {'form': form}, context)

    else:
        # if the form is invalid, render the form again with validation errors
        form = InvoiceForm()
    return render(request, 'invoice/create_invoice.html', {'form': form})
    
# Fetch and display invoices
def invoice_list(request):
    # context = {'page_title': 'Invoice List'}
    invoice = Invoice.objects.all()
    return render(request, 'invoice/invoice_list.html', {'invoice': invoice})

# Display contents of the requested invoice
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    return render(request, 'invoice/invoice_template.html', {'invoice': invoice})

def home(request):
    context = {'page_title':'Home'}
    return render(request, 'invoice/dashboard.html', context)