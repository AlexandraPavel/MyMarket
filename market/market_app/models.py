from django.conf import settings
from django.db import models

# Create your models here.'


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(MyModel):
    class Meta:
        db_table = 'customer'

    name = models.CharField(max_length=255, unique=True)
    list_products = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Product', related_name='products')

    def get_products_number(self):
        return self.list_products.count()

    def __str__(self):
        return '%s %s' % (type(self), self.id)


class Product(MyModel):
    class Meta:
        db_table = 'product'

    name = models.CharField(max_length=255, unique=True, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE(), null=True, default=1)
    details = models.CharField(max_length=255)

    def fist_name(self):
        return self.user.fist_name

    fist_name.short_description = 'Fist Name'
    fist_name.admin_order_field = 'user__fist_name'

    def last_name(self):
        return self.user.last_name

    last_name.short_description = 'Last Name'
    last_name.admin_order_field = 'user__last_name'

    def __str__(self):
        return '%s %s' % (type(self), self.id)
