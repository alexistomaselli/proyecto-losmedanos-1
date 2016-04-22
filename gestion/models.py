from django.db import models
from django.contrib import admin
# Create your models here.

#EMPLEADO/empleado
 #(El id_Empleado va desde el numero 101 al 300, el primer empleado se almacena
 # con 101 y a los siguientes se lo incrementa en 1)
class Empleado(models.Model):
 id_Empleado = models.IntegerField(primary_key=True)
 dni_Empleado = models.CharField(max_length=10)
 nombre_Empleado = models.CharField(max_length=50)
 apellido_Empleado = models.CharField(max_length=50)
 fecha_nacimiento_Empleado = models.DateField()
 telefono_Empleado = models.CharField(max_length=20)
 domicilio_Empleado = models.CharField(max_length=40)
 cuit_Empleado = models.CharField(max_length=15,blank=True)
 socio_Empleado = models.BooleanField()
 tambero_Empleado = models.BooleanField()
 porcentaje_tambo_Empleado = models.FloatField(null=True)
 sueldo_fijo_Empleado = models.FloatField(null=True)
 disponible_Empleado = models.BooleanField()


#EMPLEADO/historialEmpleado
 # (Este modelo almacena las bajas y altas del empleado)
 # (Se utiliza para calcular la antigedad)
class Historial_Empleado(models.Model):
 id_Historial_Empleado = models.IntegerField(primary_key=True)
 id_Empleado = models.IntegerField()
 fecha_ingreso_Historial_Empleado = models.DateField()
 fecha_egreso_Historial_Empleado = models.DateField(blank=True)
 motivo_egreso_Historial_Empleado = models.TextField(blank=True)

#EMPLEADO/entrega
class Entrega_Empleado(models.Model):
 id_Entrega_Empleado = models.IntegerField(primary_key=True)
 id_Empleado = models.IntegerField()
 fecha_Entrega_Empleado = models.DateField()
 monto_Entrega_Empleado = models.FloatField()
 efectivo_Entrega_Empleado = models.BooleanField()
 cheque_tercero_Entrega_Empleado = models.BooleanField()
 cheque_cuenta_corriente_Entrega_Empleado = models.BooleanField()
 numero_cheque_cuenta_corriente_Entrega_Empleado = models.CharField(max_length=20,blank=True)

#EMPLEADO/labor
class Labor_Empleado(models.Model):
 id_Labor_Empleado = models.IntegerField(primary_key=True)
 id_Empleado = models.IntegerField()
 fecha_Labor_Empleado = models.DateField()
 descripcion_Labor_Empleado = models.TextField(blank=True)
 monto_Labor_Empleado = models.FloatField()

#Empleado y Cliente-Proveedor/cuentaCte
 #(En este modelo se almacenan las cuentas de los empleados y los clientes/proveedores)
 #(Los numeros de cuenta para los empleados van desde el 1001 en adelante)
 #(Los numeros de cuenta para los CLientes/Proveedores van desde el 2001 en adelante)
class Cuenta_Corriente(models.Model):
 id_Cuenta_Corriente = models.IntegerField(primary_key=True)
 id_Persona_Cuenta_Corriente = models.IntegerField() #idPersona almacena el id del empleado o del cliente/proveedor
 numero_Cuenta_Corriente = models.IntegerField()

#EMPLEADO/liquidacion de sueldo
class Liquidacion_Sueldo(models.Model):
 id_Liquidacion_Sueldo = models.IntegerField(primary_key=True)
 id_Empleado = models.IntegerField()
 fecha_Liquidacion_Sueldo = models.DateField()
 monto_Liquidacion_Sueldo = models.FloatField()
#Liquidacion de Tambo
 #(Estos datos son utilizadon en la liquidacion de sueldo del empleado)
class Liquidacion_Tambo(models.Model):
 id_Liquidacion_Tambo = models.IntegerField(primary_key=True)
 fecha_Liquidacion_Tambo = models.DateField()
 litros_entregados_Liquidacion_Tambo = models.FloatField()
 litros_guachera_Liquidacion_Tambo = models.FloatField()
 litros_otros_Liquidacion_Tambo = models.FloatField()
 precio_por_litro_Liquidacion_Tambo = models.FloatField()


#Cliente-Proveedor
 #(El id_ClienteProveedor va desde el numero 301 en adelante, el primero se almacena
 # con 301 y a los siguientes se lo incrementa en 1)
class Cliente_Proveedor(models.Model):
 id_Cliente_Proveedor = models.IntegerField(primary_key=True)
 dni_Cliente_Proveedor = models.CharField(max_length=10,blank=True)
 nombre_Cliente_Proveedor = models.CharField(max_length=30)
 apellido_Cliente_Proveedor = models.CharField(max_length=30)
 cuit_Cliente_Proveedor = models.CharField(max_length=30,blank=True)
 telefono_Cliente_Proveedor = models.CharField(max_length=30)
 domicilio_Cliente_Proveedor = models.CharField(max_length=30)
 es_cliente_Cliente_Proveedor = models.BooleanField()
 es_proveedor_Cliente_Proveedor = models.BooleanField()
 razon_social_Cliente_Proveedor = models.CharField(max_length=30,blank=True)

 #Cliente-Proveedor/factura
 class Factura(models.Model):
  id_Factura = models.IntegerField(primary_key=True)
  id_Cliente_Proveedor = models.IntegerField()
  numero_Factura = models.CharField(max_length=20)
  tipo_Factura = models.CharField(max_length=5)
  fecha_Factura = models.DateField()
  fecha_vencimiento_Factura = models.DateField(blank=True)
  importe_neto_Factura = models.FloatField()
  importe_total_Factura = models.FloatField()
  conceptos_no_gravados_Factura = models.FloatField(null=True)


 #Factura/factura x plan de cuenta
  # (Se almacenan las relaciones entre una factura con los difrentes codigos
  # del plan de cuentas)

  class Factura_por_plan_de_cuenta(models.Model):
   id_Factura_por_plan_de_cuenta = models.IntegerField(primary_key=True)
   id_Factura = models.IntegerField()
   codigo_Plan_de_Cuentas = models.IntegerField()

  #Factura/factura x asignacion interna
   #(Se almacenan las relaciones entre una factura con los difrentes id de empleado)
  class Factura_por_asignacion_interna(models.Model):
   id_Factura_por_asignacion_interna = models.IntegerField(primary_key=True)
   id_Factura = models.IntegerField()
   id_Empleado = models.IntegerField()

  #Banco/Cuentas de los Bancos
   #(Los campos nombre_banco_Cuenta_Banco y sucursal_banco_Cuenta_Banco estan adentro de esta tabla para no crear otra tabla llamada Banco)
  class Cuenta_Banco(models.Model):
   id_Banco = models.IntegerField()
   id_Cuenta_Banco = models.IntegerField(primary_key=True)
   nombre_banco_Cuenta_Banco = models.CharField(max_length=30)
   sucursal_banco_Cuenta_Banco = models.CharField(max_length=30,blank=True)
   numero_Cuenta_Banco = models.CharField(max_length=30)
   cbu_Cuenta_Banco = models.CharField(max_length=30)
   nombre_Cuenta_Banco = models.CharField(max_length=30,blank=True)
   tipo_Cuenta_Banco = models.CharField(max_length=30,blank=True)

  class Muestra_Empleado(admin.ModelAdmin):
      list_display = ('nombre_Empleado','apellido_Empleado','dni_Empleado','fecha_nacimiento_Empleado',
      'telefono_Empleado','domicilio_Empleado','cuit_Empleado','porcentaje_tambo_Empleado','sueldo_fijo_Empleado',
      'socio_Empleado','tambero_Empleado')



admin.site.register(Empleado)
