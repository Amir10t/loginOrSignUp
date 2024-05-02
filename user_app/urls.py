from django.urls import path
from .views import LoginOrRegisterView

urlpatterns = [
    path("", LoginOrRegisterView.as_view(), name="login-or-register")
]