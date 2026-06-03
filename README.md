
# Rosa Nieve - Catálogo Digital & Sistema de Gestión

Sistema web enfocado en la exhibición interactiva de productos de maquillaje y cuidado facial para la marca **Rosa Nieve**. Este desarrollo destaca por una arquitectura limpia basada en Django, un panel de administración personalizado para el control de stock, y un diseño responsive estilizado con transiciones fluidas.

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3.12, Django Web Framework 6.0.5
* **Frontend:** HTML5, CSS3, Bootstrap 5, Animate.css
* **Base de Datos:** SQLite3 (Entorno de desarrollo local protegido mediante `.gitignore`)

## 🚀 Características Principales
* **Catálogo Dinámico:** Filtrado lógico de productos en tiempo real mediante parámetros de URL acoplados al backend (`categoria_principal`, `subcategory`).
* **Interfaz de Usuario Fluida:** Barra de navegación optimizada de alto impacto visual orientada a la experiencia de usuario (UX).
* **Módulo de Administración:** Panel administrativo nativo para la gestión y actualización del inventario de cosméticos.

## ⚙️ Instalación y Configuración Local

1. Clonar el repositorio:
```bash
git clone [https://github.com/EdisonSA/rosa_nieve_catalogo.git](https://github.com/EdisonSA/rosa_nieve_catalogo.git)
cd rosa_nieve_catalogo
```
2. Crear y activar el entorno virtual:
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
3. Instalar dependencias y ejecutar migraciones:
    pip install django
   python manage.py migrate
4. Iniciar el servidor local de desarrollo:
    python manage.py runserver

Desarrollado de forma profesional por Edison Salgado como parte de mi portafolio de TI.