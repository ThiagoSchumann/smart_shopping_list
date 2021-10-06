from django.db import models

class Supermarket(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    creation_date = models.DateField(auto_now=True, verbose_name='Data de Criação')

    class Meta:
        verbose_name = 'Supermercado'
        verbose_name_plural = 'Supermercados'

    def __str__(self):
        return self.name
