from django.utils.timezone import datetime

from django.db import models

class AuditData(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# Create your models here.
class Products(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True,
                                 related_name='products')

class Category(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Orders(AuditData):
    description = models.TextField(blank=True)
    products = models.ManyToManyField('Products', related_name='order')



