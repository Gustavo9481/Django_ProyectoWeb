from django.urls import path
from . import views

# ------------------------------ BLOG

# 1 vista principal del blog - Post generales
# 2 vista de posts filtrados por categoria
urlpatterns = [
    path('', views.blog, name="Blog"),   # 1
    path('categoria/<int:categoria_id>/', views.categorias, name="Categorias"),   # 2 - nota1
]

# nota1 > todos los caracteres de una url son texto por defecto
# se debe convertir a integer el id para que sea reconocido po la BBBDD

