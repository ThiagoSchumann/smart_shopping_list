from django.db import models

class Unit_of_measurement(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    initials = models.CharField(max_length=6, verbose_name='Sigla')
    creation_date = models.DateField(auto_now=True,verbose_name='Data de Criação')

    class Meta:
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        return self.initials