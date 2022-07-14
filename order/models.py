from django.db import models
from products.models import BaseModel, Products
# Create your models here.

class Order(BaseModel):
    #user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.first_name

    def full_name(self):
        return self.first_name + ' ' + self.last_name



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