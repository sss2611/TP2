from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('ordenes/nueva/', views.crear_orden, name='crear_orden'),
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),
    path("ordenes/<int:pk>/asignar/", views.asignar_orden, name="asignar_orden"),
]
