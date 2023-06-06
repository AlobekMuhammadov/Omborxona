from django.shortcuts import render, redirect
from django.views import View
from .models import Mahsulot
from userapp.models import Ombor

class ClientsView(View):
    def get(self,request):
        content = {
            'clientlar':Mijoz.objects.filter(ombor=Ombor.objects.filter(user=request.user))
        }
        return render(request,'clients.html',content)


class MahsulotlarView(View):
    def post(self,request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom = request.POST.get('nom'),
                brend = request.POST.get('brend'),
                o_narx = request.POST.get('o_narx'),
                s_narx = request.POST.get('s_narx'),
                miqdor = request.POST.get('miqdor'),
                olchov = request.POST.get('olchov'),
                sana = request.POST.get('sana'),
                ombor = Ombor.objects.get(user=request.user)
            )
            return redirect('mahsulotlar')
        return redirect('login')


    def get(self, request):
        if request.user.is_authenticated:
            content = {
                'mahsulotlar':Mahsulot.objects.filter(ombor=Ombor.objects.get(user=request.user))
            }
            return render(request,'products.html', content)
        return redirect('login')


# 'mahsulotlar': Mahsulot.objects.filter(ombor__id=Ombor.objects.filter(user=request.user))

class MahsulotOchirView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            Mahsulot.objects.get(id=pk, ombor__user=request.user).delete()
            return redirect('/mahsulotlar/')
        return redirect('/login/')


class MahsulotEditView(View):
    def post(self,request):
        if request.user.is_authenticated:
            Mahsulot.objects.update(
                nom = request.POST.get('nom'),
                brand = request.POST.get('brend'),
                o_narx = request.POST.get('o_narx'),
                miqdor = request.POST.get('miqdor'),
            )
            return redirect('mahsulotlar')
        return redirect('login')


    def get(self, request, pk):
        if request.user.is_authenticated:
            content ={
            'mahsulot':Mahsulot.objects.get(id=pk, ombor=Ombor.objects.get(user=request.user))
            }
            return render(request, 'product_update.html',content)
        return redirect('login')



