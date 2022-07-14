from django.db import models
# Create your models here.

def upload_image(instance, filename):
    return f"{instance.id}-{filename}"


class BaseModel(models.Model):
    created_at = models.DateTimeField('Criação:',auto_now_add=True)
    updated_at = models.DateTimeField('Atualização:',auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}"
    class Meta:
        managed = True
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')


class Products(BaseModel):
    name = models.CharField('Nome:', max_length=150)
    description = models.TextField('Descrição:')
    price = models.DecimalField('Preço:', max_digits=10, decimal_places=2)
    image = models.ImageField('Imagem:', upload_to=upload_image, null=True, blank=True)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='categories')
    slug = models.SlugField(default='')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.categoria.slug}/{self.slug}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name',)