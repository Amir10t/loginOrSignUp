from django.shortcuts import render
from django.views.generic import View
from .forms import LoginForm, RegisterForm, ResetPassword

# Create your views here.

class LoginOrRegisterView(View):
    def get(self, request):
        login_form = LoginForm()
        register_form = RegisterForm()
        reset_password_form = ResetPassword()
        context = {
            "login_form":login_form,
            "register_form": register_form,
            "reset_password_form": reset_password_form
        }
        return render(request, "user_app/loginOrRegister.html", context)