from django.contrib import admin
from django.urls import path
from asosiy.views import *
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('clients/', ClientsView.as_view(), name='clientlar'),
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mahsulot_ochir/<int:pk>/', MahsulotOchirView.as_view(), name='mahsulot_ochir'),
    path('mahsulot_edit/<int:pk>/', MahsulotEditView.as_view(), name='mahsulot_edit'),

]
