from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import OrdenDeTrabajoForm
from .models import OrdenDeTrabajo


@login_required
def crear_orden(request):
    if request.method == "POST":
        form = OrdenDeTrabajoForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.operario_creador = request.user
            orden.save()
            request.session["ultima_orden_id"] = orden.id  # Guardar en sesión
            return redirect("mantenimiento:lista_ordenes")
    else:
        form = OrdenDeTrabajoForm()
    return render(request, "mantenimiento/crear_orden.html", {"form": form})


@login_required
def lista_ordenes(request):
    if request.user.is_superuser:
        ordenes = OrdenDeTrabajo.objects.all()
    else:
        ordenes = OrdenDeTrabajo.objects.filter(operario_creador=request.user)
    return render(request, "mantenimiento/lista_ordenes.html", {"ordenes": ordenes})
