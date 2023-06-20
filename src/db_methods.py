from peewee import DoesNotExist
from src.database import postgres_connect

from src.models.bonificacion import Bonificacion
from src.models.carga import Carga
from src.models.cuenta import Cuenta
from src.models.debito import Debito
from src.models.empresa import Empresa
from src.models.peaje import Peaje
from src.models.persona import Persona
from src.models.propietario import Propietario
from src.models.tarifa import Tarifa
from src.models.telefono import Telefono
from src.models.tipo_vehiculo import TipoVehiculo
from src.models.vehiculo import Vehiculo
from src.models.ventanilla import Ventanilla
from src.models.propietario_vehiculo import PropietarioVehiculo



def nueva_carga() -> None:
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


def agregar_tarifa() -> None:
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

def agregar_peaje() -> None:
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

def agregar_ventanilla() -> None:
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

def agregar_bonificacion() -> None:
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

def nuevo_debito() -> None:
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


def Listado_de_propietarios_y_sus_vehículos() -> None:
    pass

def Listado_de_cuentas_con_su_titular_y_sus_vehículos_asociados() -> None:
    pass

def modificar_persona() -> None:
    pass

def modificar_propietario() -> None:
    pass

def modificar_cuenta() -> None:
    pass

def modificar_vehiculo() -> None:
    pass

def modificar_peaje() -> None:
    pass

def modificar_bonificacion() -> None:
    pass

def modificar_tipo_de_vehiculo() -> None:
    pass

def modificar_tarifa() -> None:
    pass
