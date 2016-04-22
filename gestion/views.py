from django.template import RequestContext
from django.template import loader, Context
from django.http import HttpResponse
from gestion.models import Empleado
from django.shortcuts import render_to_response
#from administracion.tables  import Tabla_Empleado

def Muestra_Empleados(request):
    return render(request, "muestra_empleados.html", {"Empleado": Empleado.objects.all()})
