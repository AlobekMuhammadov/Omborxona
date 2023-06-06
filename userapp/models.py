from django.contrib.auth.models import User
from django.db import models


class Ombor(models.Model):
    nom = models.CharField(max_length=70)
    ism = models.CharField(max_length=70)
    tel = models.CharField(max_length=20)
    manzil = models.CharField(max_length=50)
    soha = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}, {self.nom}"

