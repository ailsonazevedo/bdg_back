from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, verbose_name="Usuário", on_delete=models.CASCADE, related_name="user")
#     full_name = models.CharField(max_length=256, verbose_name="Nome completo")
#     phone = models.CharField(max_length=100)