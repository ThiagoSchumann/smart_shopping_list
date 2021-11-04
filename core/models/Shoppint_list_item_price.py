from django.db import models
from core.models.Shopping_list_item import Shopping_list_item
from core.models.Supermarket import Supermarket

class Shopping_list_item_price(models.Model):
    item = models.ForeignKey(Shopping_list_item, on_delete=models.CASCADE, verbose_name='Item')
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE, verbose_name='Supermercado')
    price = models.FloatField(verbose_name='Preço')

    class Meta:
        verbose_name = 'Preço do Item'
        verbose_name_plural = 'Preços dos Itens'

    def __str__(self):
        return self.name