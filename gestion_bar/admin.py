from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se verán en la tabla principal del admin
    list_display = ('nombre', 'marca', 'categoria_principal', 'subcategoria', 'precio', 'stock', 'destacado')
    
    # Filtros laterales para buscar rápido por tus nuevas secciones
    list_filter = ('categoria_principal', 'subcategoria', 'destacado')
    
    # Buscador por nombre o marca
    search_fields = ('nombre', 'marca')
