from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
class Store (Base):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='store/logo/', null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'store'
        verbose_name_plural = 'Stores'
        verbose_name = 'Store'
        ordering = ['name']