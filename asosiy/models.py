from django.db import models
from userapp.models import Ombor


class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    brend = models.CharField(max_length=50, blank=True)
    o_narx = models.PositiveSmallIntegerField()
    s_narx = models.PositiveSmallIntegerField()
    miqdor = models.CharField(max_length=100)
    olchov = models.CharField(max_length=30)
    sana = models.DateField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}, {self.s_narx}"


class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=20)
    manzil = models.CharField(max_length=100, blank=True, null=True)
    qarz = models.PositiveSmallIntegerField(default=0)
    ombor = models.ForeignKey(Ombor,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}, {self.qarz}"

