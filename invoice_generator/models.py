from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    company_name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    description = models.TextField(max_length=200)
    paid = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.id} for {self.client}"
