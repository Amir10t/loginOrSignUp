from django.urls import path
from .views import *

urlpatterns = [
    path("", LoginOrRegisterView.as_view(), name="login-or-register"),
    path("login_operator", login_operator, name="login-operator"),
    path("register_operator", register_operator, name="register-operator"),
    path("reset_password_operator", reset_password_operator, name="reset-password-operator")
]