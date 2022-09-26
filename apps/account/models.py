from django.db import models
from django.contrib.auth.models import User
from apps.order.models import Region



class Client(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuário", on_delete=models.CASCADE, related_name="user")
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    full_name = models.CharField("Nome completo:", max_length=256, default='', null=False)
    phone = models.CharField("Telefone:",max_length=100, default='', null=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ('-full_name',)

class Address(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE, verbose_name="Usuário", null=True, blank=True)
    name = models.CharField('Nome do endereço:',max_length=100, null=True, blank=True)
    street = models.CharField('Rua:', max_length=100, default='', null=True, blank=True)
    zipcode = models.CharField('CEP:', max_length=100, default='', null=True)
    number = models.CharField('Número:', max_length=50, default='', null=True, blank=True)
    district = models.CharField('Bairro:', max_length=100, default='', null=True, blank=True)
    complement = models.CharField('Complemento:', max_length=100, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Adresses'