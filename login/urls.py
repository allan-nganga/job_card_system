from django.urls import include, path
from .views import authView, dashboard, LoginView

urlpatterns = [
    path("", LoginView.as_view(), name='login'), # Root URL redirects to login
    path("dashboard/", dashboard, name='dashboard'), # URL for dashboard
    path("signup/", authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
]