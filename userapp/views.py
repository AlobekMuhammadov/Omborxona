from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .models import *
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username= request.POST.get('login'),
            password = request.POST.get('password')
            )
        if user is None:
            # messages.error(request, 'login yoki parolda hatolik bor')
            return redirect('login')
        login(request, user)
        return redirect('bolimlar')
    return render(request,'home.html')


def logout_view(request):
    logout(request)
    return redirect('logout')

class BolimlarView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,'bulimlar.html')
        return redirect('login')












































































