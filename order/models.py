from django.db import models
from products.models import BaseModel, Products
from account.models import Profile

class Region(models.Model):
    name = models.CharField('Nome da Região:', max_length=80)
    shipping_price = models.DecimalField('Preço do Frete:', max_digits=10, decimal_places=2, null=False)

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

class Additional(BaseModel):
    name = models.CharField('Nome do Item Adicional:', max_length=100)
    price = models.DecimalField('Preço do Item Adicional:', max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Additional'
        verbose_name_plural = 'Additionals'
        ordering = ('-name',)

class OrderItem(models.Model):
    product = models.ForeignKey(Products, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantidade:', default=1)        
    price = models.DecimalField('Preço:', max_digits=9, decimal_places=2, default=0, null=False)
    created_at = models.DateTimeField('Criação:',auto_now_add=True)
    note = models.TextField('Observação:', max_length=255, blank=True, null=True)
    additional = models.ManyToManyField(Additional, blank=True)
    
    def __str__(self):
        return '%s' % self.product

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
        ordering = ('-created_at',)

class Order(BaseModel):
    
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("M", "Preparando pedido"),
        ("E", "Saiu para entrega"),
        ("F", "Pedido Entregue")
    )
    user = models.ForeignKey(Profile, related_name='orders', on_delete=models.CASCADE, default='')
    order_items = models.ManyToManyField(OrderItem)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default='')
    status = models.CharField("Status do Pedido:",max_length=1, choices=STATUS_CHOICES, blank=False, null=False, default="P")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default='')

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




