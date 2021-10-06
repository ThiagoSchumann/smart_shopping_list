from django.contrib import admin
from core.models import Unit_of_measurement, Product, Supermarket

# Register your models here.

class Unit_of_measurement_admin(admin.ModelAdmin):
    list_display = ('id', 'initials', 'name')

class Product_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit_of_measurement')

class Supermarket_admin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Unit_of_measurement, Unit_of_measurement_admin)
admin.site.register(Product, Product_admin)
admin.site.register(Supermarket, Supermarket_admin)