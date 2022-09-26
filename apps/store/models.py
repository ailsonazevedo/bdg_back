from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
class Store (Base):
    name = models.CharField('Nome da loja:', max_length=100)
    logo = models.ImageField('Logo da loja:', upload_to='store/logo/', null=True, blank=True)
    address = models.CharField('Endereço:', max_length=100)
    city = models.CharField('Cidade:', max_length=100)
    state = models.CharField('Estado:', max_length=100)
    zipcode = models.CharField('CEP:', max_length=100)
    phone = models.CharField('Telefone:', max_length=100, help_text='Este numero será utilizado para efetuar o envio dos pedidos')
    email = models.CharField('Email:', max_length=100)

    def __str__(self):
        return self.name
    
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

    class Meta:
        db_table = 'store'
        verbose_name_plural = 'Stores'
        verbose_name = 'Store'
        ordering = ['name']