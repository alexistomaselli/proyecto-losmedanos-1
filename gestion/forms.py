from django import forms
from .models import Empleado

    class EmpleadoForm(forms.ModelForm):

        class Meta:
            model = Empleado
            fields = ('nombre_Empleado','apellido_Empleado','dni_Empleado','fecha_nacimiento_Empleado',
            'telefono_Empleado','domicilio_Empleado','cuit_Empleado','porcentaje_tambo_Empleado','sueldo_fijo_Empleado',
            'socio_Empleado','tambero_Empleado')
