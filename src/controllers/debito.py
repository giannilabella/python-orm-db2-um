from src.database import postgres_connect
from src.database import mongodb_connect, postgres_connect
from src.models.debito import Debito
from src.models.cuenta import Cuenta
from src.models.peaje import Peaje
from src.models.vehiculo import Vehiculo
from src.models.ventanilla import Ventanilla
from datetime import datetime


def agregar_debito() -> Debito:
    try:
        mongo_database = mongodb_connect()
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    cuenta_id: str = input("Ingrese cuenta vinculada: ")
    peaje_nombre: str = input("Ingrese nombre de peaje: ")
    ventanilla_id: str = input("Ingrese identificador de ventanilla: ")
    vehiculo_matricula: str = input("Ingrese matricula del vehículo: ")
    
    try:
        cuenta = Cuenta.get(Cuenta.cuenta_id==cuenta_id)
        peaje = Peaje.get(Peaje.peaje_nombre==peaje_nombre)
        ventanilla = Ventanilla.get(Ventanilla.ventanilla_id==ventanilla_id)
        vehiculo = Vehiculo.get(Vehiculo.vehiculo_matricula==vehiculo_matricula)
    except Exception as e:
        database.close()
        print('Error buscando cuenta')
        print(e)
        input('Presione enter para continuar...')
        return

    tarifa: str = input("ingrese tarifa")

    try:
        beneficio = mongo_database.Bonificaciones.find({"cuenta":cuenta.cuenta_id,"peaje":peaje.peaje_id})
        descuento = 1 - int(beneficio[0]["descuento"].removesuffix("%"))/100
        new_debito:Debito = Debito.create(
            debito_fecha_y_hora = datetime.now(),
            debito_cuenta = cuenta,
            debito_peaje = peaje,
            debito_vehiculo = vehiculo,
            debito_ventanilla = ventanilla,
            debito_monto = int(tarifa)*descuento
        )
        cuenta.cuenta_saldo -= new_debito.debito_monto
        cuenta.save()
        database.close()
        print('Debito creado')
        input('Presione enter para continuar...')
        return new_debito
    except Exception as e:
        database.close()
        print('Error creando Debito')
        print(e)
        input('Presione enter para continuar...')
        return