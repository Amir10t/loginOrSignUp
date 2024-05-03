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

def register_operator(request: HttpRequest):
    register_form = RegisterForm(request.POST)
    if (register_form.is_valid()):
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        repeat_password = register_form.cleaned_data.get("repeat_password")
        if User.objects.filter(email=email).exists() == False:
            if password == repeat_password:
                new_user = User(email=email)
                new_user.set_password(password)
                new_user.save()
            else:
                register_form.add_error("repeat_password", "pass != repeat pass")
        else:
            register_form.add_error("email", "Enter a new Email")

        context = {
            "register_from":register_form
        }

        return render(request, "user_app/loginOrRegister.html", context)