from django.db import models
from django.contrib.auth.models import User

from order.models import Region

class Client(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuário", on_delete=models.CASCADE, related_name="user")
    full_name = models.CharField("Nome completo:", max_length=256, default='',null=False)
    phone = models.CharField("Telefone:",max_length=100, default='',null=False)
    address = models.CharField('Endereço:', max_length=100, default='',null=False)
    zipcode = models.CharField('CEP:', max_length=100, default='')
    number = models.CharField('Número:', max_length=50, default='')
    district = models.CharField('Bairro:', max_length=100, default='')
    complement = models.CharField('Complemento:', max_length=100, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ('-full_name',)