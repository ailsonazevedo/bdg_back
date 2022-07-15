from django.db import models
from products.models import BaseModel, Products
# Create your models here.
class Region(models.Model):
    name = models.CharField('Nome da Região:', max_length=80)
    shipping_price = models.DecimalField('Preço do Frete:', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-name',]
    
    def __str__(self):
        return self.name

class Order(BaseModel):
    #user = models.ForeignKey("account.Profile", related_name='orders', on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    #email = models.CharField(max_length=100)
    address = models.CharField('Endereço:', max_length=100, default='')
    zipcode = models.CharField('CEP:', max_length=100, default='')
    number = models.CharField('Número:',max_length=50, default='')
    district = models.CharField('Bairro:', max_length=100, default='')
    complement = models.CharField('Complemento:', max_length=100, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default='')
    #phone = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.address




class OrderItem(models.Model):

    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("M", "Preparando pedido"),
        ("E", "Saiu para entrega")
    )

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantidade:', default=1)        
    price = models.DecimalField('Preço:', max_digits=9, decimal_places=2, default=0)
    created_at = models.DateTimeField('Criação:',auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False, default="P")

    def __str__(self):
        return '%s' % self.id

    # def total(self):
    #     return self.product.price * self.quantity

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
        ordering = ('-created_at',)