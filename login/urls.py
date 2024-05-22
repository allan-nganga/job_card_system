from django.urls import include, path
from .views import authView, dashboard, LoginView
from invoice_generator.views import home

urlpatterns = [
    path("dashboard/invoices/", home, name='home'),
    path("", LoginView.as_view(), name='login'), # Root URL redirects to login
    path("dashboard/", dashboard, name='dashboard'), # URL for dashboard
    path("signup/", authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
]