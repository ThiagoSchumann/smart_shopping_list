from django.db import models
from core.models.Unit_of_measurement import Unit_of_measurement

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    unit_of_measurement = models.ForeignKey(Unit_of_measurement, on_delete=models.CASCADE,verbose_name='Unidade de Medida')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name