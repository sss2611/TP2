# ITSE -- Patrimonio 2025

# Link : https://tp2-sandra-django.onrender.com/

**Materia:** Programación IV  
**Profesora:** Maria de los Angeles Perez
**Trabajo Práctico Nº 2**  
**Estudiante:** Sandra Soledad Sanchez  
**Carrera:** Tecnicatura Superior en Desarrollo de Software  
**Año:** 2025

---

## Estructura
TP2_SandraSanchez/
├── app/
│         ├── app/             
│         ├── manage.py
│         ├── settings.py
│         ├── wsgi.py
│         ├── asgi.py
│         └── __init__.py
├── cuentas/
├── mantenimiento/
├── requirements.txt es mi estructura

## Objetivo del Proyecto

Desarrollar una aplicación web institucional en Django que permita gestionar usuarios, áreas temáticas y contenidos patrimoniales, aplicando principios de autenticación, autorización, control de acceso y lógica de negocio. El sistema se adapta al espíritu del práctico original (MantenimientoFlow) desde una perspectiva institucional y educativa.

---

## Cumplimiento de Requisitos del Práctico

| Requisito                  | Implementación en Patrimonio 2025 |
|---------------------------|------------------------------------|
| **Autenticación**         | Login personalizado con validación de acceso (`admitido`, `is_staff`, `superuser`) |
| **Autorización por rol**  | Control dinámico de acceso según el campo `area` y el estado `admitido` |
| **Gestión de usuarios**   | Registro, edición, eliminación, admisión y segmentación por área |
| **Panel administrativo**  | Acceso restringido a usuarios con área “Staff” o superusuarios |
| **ORM**                   | Consultas con `filter()`, `get_object_or_404()`, `save()`, `delete()` |
| **Formularios**           | `UserEditForm` para edición de usuarios con campos extendidos |
| **Mensajes y validaciones** | Validación de unicidad, control de contraseña, mensajes de error personalizados |
| **Extensibilidad**        | App `mantenimiento` creada para futuras funcionalidades técnicas (órdenes, suministros) |
| **Contenido institucional** | Gestión de noticias, secciones temáticas (Historia, Bellas Artes, Antropología) |

---

## Justificación Académica

El sistema Patrimonio 2025 cumple con los objetivos pedagógicos del práctico al demostrar dominio de Django en:

- Modelado de usuarios personalizados  
- Control de acceso por rol y estado  
- Uso del ORM para lógica de negocio  
- Implementación de vistas protegidas y formularios validados  
- Modularidad y extensibilidad del sistema  

Aunque no replica literalmente el flujo de mantenimiento industrial, adapta sus principios a un contexto institucional real, con potencial de crecimiento hacia funcionalidades técnicas mediante la app `mantenimiento`.

---

## Extensiones posibles

- Modelos `OrdenDeTrabajo`, `Suministro`, `ConsumoSuministro`  
- Formularios con validaciones condicionales  
- Reportes por área o actividad  
- Dashboard para administradores  
- Control de inventario y trazabilidad de tareas  
- Segmentación por roles operativos (Operario, Jefe de Taller, Administrador)

## App `mantenimiento` incluida

El proyecto incluye la app `mantenimiento` como base para extender el sistema hacia funcionalidades técnicas de gestión de órdenes, suministros y consumos. Esta app está registrada y preparada para incorporar modelos, formularios y vistas alineadas con el flujo de trabajo del práctico original.