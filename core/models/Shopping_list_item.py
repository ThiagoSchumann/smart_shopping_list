from django.db import models

class Shopping_list_item(models.Model):
    creation_date = models.DateField(auto_now=True, verbose_name='Data de Criação')

    class Meta:
        verbose_name = 'Item da Lista'
        verbose_name_plural = 'Itens Das Listas'

    def __str__(self):
        return self.name