from database import postgres_database
from peewee import *

from models.basemodel import *
from models.bonificacion import *
from models.carga import *
from models.cuenta import *
from models.debito import *
from models.empresa import *
from models.peaje import *
from models.persona import *
from models.propietario import *
from models.tarifa import *
from models.telefono import *
from models.tipovehiculo import *
from models.vehiculo import *
from models.vehiculo import *
from models.ventanilla import *

def agregar_persona():

    dni:str             = input("ingrese dni (sin puntos ni guion): ")
    nombre_1:str        = input("ingrese primer nombre: ")
    nombre_2:str        = input("ingrese segundo nombre: ")
    direccion:str       = input("ingrese dirección: ")
    apellido_1:str      = input("ingrese primer apellido: ")
    apellido_2:str      = input("ingrese segundo apellido: ")
    mail:str            = input("ingrese e-mail: ")
    celular:str         = input("ingrese celular: ")

    hay_persona_asociada:str   = input("tiene personas asociadas (y/n): ")
    hay_persona_asociada       = hay_persona_asociada.lower()
    asociado = None

    if(hay_persona_asociada in ["y","yes","y/","yes/","si","si/"]):
        tmp_dni:str   = input("ingrese el dni de la persona asociada: ")
        try:
            temp_persona  = Persona.get(Persona.persona_dni==tmp_dni)
            asociado      = temp_persona.persona_id
        except DoesNotExist:
            input("No existe una persona con ese dni, presione enter para continuar...")
            return
        
    elif(hay_persona_asociada not in ["n","no","n/","no/"]):
        input("entrada no valida, toque cualquier tecla para continuar...")
        return

    try:
        new_persona = Persona.create(
            persona_dni         = dni,
            persona_nombre_1    = nombre_1,
            persona_nombre_2    = nombre_2,
            persona_direccion   = direccion,
            persona_apellido_1  = apellido_1,
            persona_apellido_2  = apellido_2,
            persona_mail        = mail,
            persona_celular     = celular,
            persona_dni_asociado= asociado,
            )
    except Exception:
        input("dato no valido ingresado para algún dato pedido, toque enter para continuar...")
        return
    else:
        input("transacción realizada exitosamente, toque enter para continuar...")
    
def agregar_empresa():
    rut:str = input("Ingrese RUT (sin puntos ni guion): ")
    nombre:str = input("Ingrese nombre: ")
    direccion = input("Ingrese direccion: ")

    try:
        new_empresa = Empresa.create(
            empresa_rut=rut,
            empresa_nombre=nombre,
            empresa_direccion=direccion
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def agregar_telefono():
    numero = input("Ingrese numero de telefono: ")
    empresa_rut = input("Ingrese RUT de empresa asociada: ")

    try:
        new_telefono = Telefono.create(
            telefono_numero=numero,
            telefono_empresa_rut=empresa_rut
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def agregar_propietario():
    persona_id = input("Ingrese ID de persona: ")
    empresa_id = input("Ingrese ID de empresa: ")

    try:
        new_propietario = Propietario.create(
            propietario_persona_id=persona_id,
            propietario_empresa_id=empresa_id
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def agregar_cuenta():
    creacion = input("Ingrese fecha de creacion (YYYY-MM-DD): ")
    saldo = input("Ingrese saldo: ")
    propietario_id = input("Ingrese ID de propietario: ")

    try:
        new_cuenta = Cuenta.create(
            cuenta_creacion=creacion,
            cuenta_saldo=saldo,
            cuenta_propietario_id=propietario_id
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def nueva_carga():
    cuenta_numero = input("Ingrese numero de cuenta: ")
    fecha_y_hora = input("Ingrese fecha y hora (YYYY-MM-DD HH:MM:SS): ")
    importe = input("Ingrese importe: ")

    try:
        new_carga = Carga.create(
            carga_cuenta_numero=cuenta_numero,
            carga_fecha_y_hora=fecha_y_hora,
            carga_importe=importe
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def agregar_tipo_vehiculo():
    tipo = input("Ingrese tipo de vehiculo: ")

    try:
        new_tipo_vehiculo = TipoVehiculo.create(
            tipo_vehiculo_tipo=tipo
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def agregar_vehiculo():
    matricula = input("Ingrese matricula: ")
    marca = input("Ingrese marca: ")
    modelo = input("Ingrese modelo: ")
    color = input("Ingrese color: ")
    id_rfid = input("Ingrese ID RFID: ")
    tipo_id = input("Ingrese ID de tipo de vehiculo: ")

    try:
        new_vehiculo = Vehiculo.create(
            vehiculo_matricula=matricula,
            vehiculo_marca=marca,
            vehiculo_modelo=modelo,
            vehiculo_color=color,
            vehiculo_id_rfid=id_rfid,
            vehiculo_tipo_id=tipo_id
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def agregar_tarifa():
    tipo_vehiculo_id = input("Ingrese ID de tipo de vehiculo: ")
    fecha = input("Ingrese fecha (YYYY-MM-DD): ")
    valor = input("Ingrese valor: ")

    try:
        new_tarifa = Tarifa.create(
            tarifa_tipo_vehiculo_id=tipo_vehiculo_id,
            tarifa_fecha=fecha,
            tarifa_valor=valor
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def agregar_peaje():
    nombre = input("Ingrese nombre de peaje: ")
    ruta = input("Ingrese ruta: ")
    kilometro = input("Ingrese kilometro: ")
    telefono = input("Ingrese telefono: ")
    cantidad_ventanillas = input("Ingrese cantidad de ventanillas: ")

    try:
        new_peaje = Peaje.create(
            peaje_nombre=nombre,
            peaje_ruta=ruta,
            peaje_kilometro=kilometro,
            peaje_telefono=telefono,
            peaje_cantidad_ventanillas=cantidad_ventanillas
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def agregar_ventanilla():
    peaje_id = input("Ingrese ID de peaje: ")
    numero = input("Ingrese numero de ventanilla: ")
    es_rfid = input("Es RFID (True/False): ")

    try:
        new_ventanilla = Ventanilla.create(
            ventanilla_peaje_id=peaje_id,
            ventanilla_numero=numero,
            ventanilla_es_rfid=es_rfid
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def agregar_bonificacion():
    cuenta_numero = input("Ingrese numero de cuenta: ")
    fecha_otorgo = input("Ingrese fecha de otorgamiento (YYYY-MM-DD): ")
    descuento = input("Ingrese descuento (%): ")
    motivo = input("Ingrese motivo: ")
    peaje_id = input("Ingrese ID de peaje: ")
    fecha_renovacion = input("Ingrese fecha de renovacion (YYYY-MM-DD): ")

    try:
        new_bonificacion = Bonificacion.create(
            bonificacion_cuenta_numero=cuenta_numero,
            bonificacion_fecha_otorgo=fecha_otorgo,
            bonificacion_descuento=descuento,
            bonificacion_motivo=motivo,
            bonificacion_peaje_id=peaje_id,
            bonificacion_fecha_renovacion=fecha_renovacion
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return

def nuevo_debito():
    vehiculo_id = input("Ingrese ID de vehiculo: ")
    peaje_id = input("Ingrese ID de peaje: ")
    ventanilla_numero = input("Ingrese numero de ventanilla: ")
    fecha_y_hora = input("Ingrese fecha y hora (YYYY-MM-DD HH:MM:SS): ")
    cuenta_numero = input("Ingrese numero de cuenta: ")

    try:
        new_debito = Debito.create(
            debito_vehiculo_id=vehiculo_id,
            debito_peaje_id=peaje_id,
            debito_ventanilla_numero=ventanilla_numero,
            debito_fecha_y_hora=fecha_y_hora,
            debito_cuenta_numero=cuenta_numero
        )
    except Exception:
        input("Dato no valido ingresado para algún dato pedido")
        return


def Listado_de_propietarios_y_sus_vehículos():
    pass

def Listado_de_cuentas_con_su_titular_y_sus_vehículos_asociados():
    pass

def modificar_persona():
    pass

def modificar_propietario():
    pass

def modificar_cuenta():
    pass

def modificar_vehiculo():
    pass

def modificar_peaje():
    pass

def modificar_bonificacion():
    pass

def modificar_tipo_de_vehiculo():
    pass

def modificar_tarifa():
    pass
