from django.db import models


class TaxModel(models.Model):
    tax = models.FloatField('Tax')

    def __str__(self):
        return '{} %'.format(self.tax)


class ProductModel(models.Model):
    name = models.CharField('Product name', max_length=50)
    price = models.FloatField('Price', default=0.0)
    tax = models.ForeignKey(TaxModel, on_delete=models.SET_NULL, null=True)
