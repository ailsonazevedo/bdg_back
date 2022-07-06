from django.db import models



class BaseModel(models.Model):
    created_at = models.DateTimeField('Criação:',auto_now_add=True)
    updated_at = models.DateTimeField('Atualização:',auto_now=True)


class Products(BaseModel):
    name = models.CharField('Nome:',max_length=100)
    description = models.TextField('Descrição:')
    price = models.DecimalField('Preço:',max_digits=10, decimal_places=2)
    image = models.ImageField('Imagem:',upload_to='media/products', null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name',)


# Create your models here.
