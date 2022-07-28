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

class Payment(models.Model):
    name = models.CharField('Tipo do pagamento', max_length=50)
    description = models.CharField('Descrição do pagamento', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ('-name',)

class OrderItem(models.Model):

    #order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantidade:', default=1)        
    price = models.DecimalField('Preço:', max_digits=9, decimal_places=2, default=0)
    created_at = models.DateTimeField('Criação:',auto_now_add=True)
    

    def __str__(self):
        return '%s' % self.product

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
        ordering = ('-created_at',)

class Order(BaseModel):
    #user = models.ForeignKey("account.Profile", related_name='orders', on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("M", "Preparando pedido"),
        ("E", "Saiu para entrega"),
        ("F", "Pedido Entregue")
    )

    order_items = models.ManyToManyField(OrderItem)
    full_name = models.CharField("Nome completo:", max_length=256, default='')
    address = models.CharField('Endereço:', max_length=100, default='')
    zipcode = models.CharField('CEP:', max_length=100, default='')
    number = models.CharField('Número:', max_length=50, default='')
    district = models.CharField('Bairro:', max_length=100, default='')
    complement = models.CharField('Complemento:', max_length=100, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default='')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default='')
    phone = models.CharField("Telefone:",max_length=100, default='')
    status = models.CharField("Status do Pedido:",max_length=1, choices=STATUS_CHOICES, blank=False, null=False, default="P")

    def clean_zipcode(self):
        data = self.cleaned_data["zipcode"]
        data = data.replace("-", "")
        data = data.replace(".", "")
        return data

    def clean_phone(self):
        data = self.cleaned_data["phone"]
        data = data.replace("(", "")
        data = data.replace(")", "")
        data = data.replace("-", "")
        return data

    def get_status_choices(self):
        return [i[1] for i in Order._meta.get_field('status').choices if i[0] == self.status][0]

    def get_order_items(self):
        if self.order_items.all():
            return list(self.order_items.all().values_list('id', flat=True))
        else:
            return 'NA'

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.full_name + ' fez um pedido para '+ self.address + ',' + self.number + ' - ' + self.district




