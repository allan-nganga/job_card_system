from django.urls import include, path
from .views import authView, home, LoginView

urlpatterns = [
    path("", LoginView.as_view(), name='login'), # Root URL redirects to login
    path("signup/", authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
]