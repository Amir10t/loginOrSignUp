from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class LoginOrRegisterView(View):
    def get(self, request):
        context = {}
        return render(request, "user_app/loginOrRegister.html", context)