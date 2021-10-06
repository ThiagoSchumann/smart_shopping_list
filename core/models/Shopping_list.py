from django.db import models

class Shopping_list(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    expected_date = models.DateField(verbose_name='Data Prevista')
    creation_date = models.DateField(auto_now=True, verbose_name='Data de Criação')


