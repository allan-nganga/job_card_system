from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import Invoice
from .forms import InvoiceForm

# Create your views here.
def invoice(request):
    return render(request, 'invoice_template.html', {})

def generate_invoice_pdf(request, invoice_id):
    # Retrieve the invoice object
    invoice = Invoice.objects.get(id=invoice_id)

    # Render the HTML template with invoice data
    # template = get_template('invoice/invoice_template.html')
    html_string = render_to_string('invoices/invoice_template.html', {'invoice': invoice})

    # Create a PDF file using WeasyPrint
    pdf_file = HTML(string=html_string).write_pdf()

    # Create a HTTP response with PDF as content type
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=invoice_{invoice.invoice_number}.pdf'
    return response

# invoice generate function
def generate_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
        else:
            form = InvoiceForm()
        return render(request, 'invoice/invoice_list.html', {'form': form})
    
# invoice list view function
# def invoice_list(request):
  #   invoices = Invoice.objects.all()
  #   return render(request, 'invoices/invoice_list.html', {'invoices': invoices})

# Dashboard function
def dashboard(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices/dashboard.html', {'invoices': invoices})