from django.shortcuts import render

# Create your views here.
def invoice(request):
    return render(request, 'invoice_template.html', {})