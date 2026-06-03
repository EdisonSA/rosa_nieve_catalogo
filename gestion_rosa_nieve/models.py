from django.db import models

class Producto(models.Model):
    # Categorías Principales
    CATEGORIAS_PRINCIPALES = [
        ('makeup', 'MAKEUP'),
        ('sexy_hot', 'SEXY - HOT'),
        ('fragance', 'FRAGANCE'),
    ]

    # Subcategorías agrupadas
    SUBCATEGORIAS = [
        # MAKEUP
        ('ojos', 'OJOS'),
        ('labios', 'LABIOS'),
        ('piel', 'PIEL'),
        
        # SEXY - HOT
        ('lenceria_sexy', 'LENCERÍA SEXY'),
        
        # FRAGANCE
        ('dulces', 'DULCES'),
        ('citricas', 'CÍTRICAS'),
        ('amaderadas', 'AMADERADAS'),
    ]

    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Clasificación doble para los productos de Rosa Nieve
    categoria_principal = models.CharField(max_length=20, choices=CATEGORIAS_PRINCIPALES, default='makeup')
    subcategoria = models.CharField(max_length=20, choices=SUBCATEGORIAS, default='piel')
    
    stock = models.IntegerField(default=0)
    destacado = models.BooleanField(default=False) 

    def __str__(self):
        return f"[{self.get_categoria_principal_display()}] {self.nombre} - {self.marca if self.marca else ''}"

    # BOTONES DE ACCION
    class Meta:
        db_table = 'gestion_bar_producto'  # OBLIGA A DJANGO A USAR LA TABLA ACTUAL CON LOS 15 PRODUCTOS
