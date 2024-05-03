from django.urls import path
from .views import *

urlpatterns = [
    path("", LoginOrRegisterView.as_view(), name="login-or-register"),
    path("login_operator", login_operator, name="login-operator")
]