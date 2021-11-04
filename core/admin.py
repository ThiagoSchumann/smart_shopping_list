from django.contrib import admin
from core.models import Unit_of_measurement, Product, Supermarket, Shopping_list

# Register your models here.

class Unit_of_measurement_admin(admin.ModelAdmin):
    list_display = ('id', 'initials', 'name')

class Product_admin(admin.ModelAdmin):
    list_display = ('id', 'name')

class Supermarket_admin(admin.ModelAdmin):
    list_display = ('id', 'name')

class teste(admin.TabularInline):
    model = Product

class Shopping_list_admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [
        teste
    ]

admin.site.register(Unit_of_measurement, Unit_of_measurement_admin)
admin.site.register(Product, Product_admin)
admin.site.register(Supermarket, Supermarket_admin)
admin.site.register(Shopping_list, Shopping_list_admin)