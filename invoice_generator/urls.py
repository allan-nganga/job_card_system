from django.urls import path
from .views import invoice

urlpatterns = [
    path('invoice/', invoice, name='invoice'),
]