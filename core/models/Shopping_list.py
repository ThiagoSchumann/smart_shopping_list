from django.db import models
from core.models.Shopping_list_item import Shopping_list_item
from core.models.Product import Product

class Shopping_list(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    expected_date = models.DateField(verbose_name='Data Prevista')
    creation_date = models.DateField(auto_now=True, verbose_name='Data de Criação')
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Lista de Compra'
        verbose_name_plural = 'Listas de Compras'

    def __str__(self):
        return self.name