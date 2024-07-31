from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('crear/', views.crear_registro, name='crear_registro'),
    path('', views.listar_registros, name='listar_registros'),
    path('registro/', views.registro, name='registro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Ruta para cerrar sesión
]
