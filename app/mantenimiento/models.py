from django.db import models
from cuentas.models import CustomUser

class Suministro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.stock} disponibles)"

class OrdenDeTrabajo(models.Model):
    PRIORIDAD_CHOICES = [('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')]
    ESTADO_CHOICES = [('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Cerrada', 'Cerrada')]

    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion_falla = models.TextField()
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    operario_creador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ordenes_creadas')
    operario_asignado = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='ordenes_asignadas')
    fecha_cierre_real = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.estado}"

class ConsumoSuministro(models.Model):
    orden_de_trabajo = models.ForeignKey(OrdenDeTrabajo, on_delete=models.CASCADE)
    suministro = models.ForeignKey(Suministro, on_delete=models.CASCADE)
    cantidad_usada = models.PositiveIntegerField()
    fecha_consumo = models.DateField()

    def __str__(self):
        return f"{self.cantidad_usada} de {self.suministro.nombre} en {self.orden_de_trabajo.titulo}"
