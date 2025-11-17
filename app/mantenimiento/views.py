from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AsignarOrdenForm, OrdenDeTrabajoForm
from .models import OrdenDeTrabajo
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def crear_orden(request):
    if request.method == "POST":
        form = OrdenDeTrabajoForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.operario_creador = request.user
            orden.save()
            request.session["ultima_orden_id"] = orden.id  # Guardar en sesión

            messages.success(request, "La orden se guardó correctamente.")

            return redirect("mantenimiento:lista_ordenes")

    else:
        form = OrdenDeTrabajoForm()
    return render(request, "mantenimiento/crear_orden.html", {"form": form})


@login_required
def lista_ordenes(request):
    if request.user.is_staff or request.user.is_superuser:
        ordenes = OrdenDeTrabajo.objects.all()
    else:
        ordenes = OrdenDeTrabajo.objects.filter(operario_creador=request.user)
    return render(request, "mantenimiento/lista_ordenes.html", {"ordenes": ordenes})

@staff_member_required
def asignar_orden(request, pk):
    orden = get_object_or_404(OrdenDeTrabajo, pk=pk)
    if request.method == "POST":
        form = AsignarOrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect("mantenimiento:lista_ordenes")
    else:
        form = AsignarOrdenForm(instance=orden)
    return render(request, "mantenimiento/asignar_orden.html", {"form": form, "orden": orden})