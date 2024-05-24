import html
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Invoice
from .forms import InvoiceForm

# Create your views here.
def invoice(request):
    return render(request, 'invoice_template.html', {})


# Generate PDF
def generate_invoice_pdf(request, invoice_id):
    # Retrieve the invoice object
    try:
        invoice = Invoice.objects.get(id=invoice_id)
    except Invoice.DoesNotExist:
        return HttpResponse("Invoice not found!", status=404)

    # Prepare context data for the template
    context = {
        'invoice': {
            'number': invoice.id,
            'client_name': invoice.client_name,
            'company_name': invoice.company_name,
            'billing_address': invoice.billing_address,
            'item_description': invoice.item_description,
            'item_quantity': invoice.item_quantity,
            'item_price': invoice.item_price,  
            'due_date': invoice.due_date, 
        }
    }

    # Render the HTML template with invoice data
    # template = get_template('invoice/invoice_template.html')
    html_string = render_to_string('invoice/invoice_template.html', context)

    # Create a PDF file using WeasyPrint
    # pdf_file = weasyprint.HTML(string=html_string).write_pdf(stylesheets=[weasyprint.css('login/static/invoice/style.css')])
    html = HTML(string =html_string)
    pdf = html.write_pdf()

    # Create a HTTP response with PDF as content type
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'
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