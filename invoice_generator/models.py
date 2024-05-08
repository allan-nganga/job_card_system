from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_number = models.IntegerField(max_length=20)
    pub_date = models.DateTimeField("date published")
    due_date = models.DateField("due date")
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=200)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
