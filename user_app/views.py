from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from .forms import LoginForm, RegisterForm, ResetPassword


# Create your views here.

class LoginOrRegisterView(View):
    def get(self, request):
        login_form = LoginForm()
        register_form = RegisterForm()
        reset_password_form = ResetPassword()
        context = {
            "login_form": login_form,
            "register_form": register_form,
            "reset_password_form": reset_password_form
        }
        return render(request, "user_app/loginOrRegister.html", context)


def login_operator(request: HttpRequest):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        email = login_form.cleaned_data.get("email")
        password = login_form.cleaned_data.get("password")
        user: User = User.objects.filter(email=email).first()
        if(user is not None):
            if user.check_password(password):
                login(request, user)
                return HttpResponse("Welcome Back!")
            else:
                login_form.add_error("password","Your Pass is not Correct")
        else:
            return HttpResponse("There is No User")

        context = {
            "login_form":login_form
        }

        return render(request, "user_app/loginOrRegister.html", context)