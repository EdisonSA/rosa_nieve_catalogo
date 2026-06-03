from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gestion_rosa_nieve import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.menu_bar, name='menu'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar_del_carrito"),
    path('limpiar/', views.limpiar_carrito, name="limpiar_carrito"),
    path('sumar/<int:producto_id>/', views.sumar_unidad, name="sumar_unidad"),
    path('restar/<int:producto_id>/', views.restar_unidad, name="restar_unidad"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
