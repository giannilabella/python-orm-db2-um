from src.database import mongodb_connect, postgres_connect
from src.models.debito import Debito
from src.models.cuenta import Cuenta
from src.models.propietario import Propietario
from src.models.persona import Persona
from src.models.empresa import Empresa
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

    desea: str = input('Desea debitar de cuenta de Persona o Empresa (p/e): ').lower()
    (cuenta, peaje) = get_cuenta_y_peaje(database, desea)

    ventanillas_list = list(map(lambda v: v.ventanilla_id, peaje.ventanillas))
    print(f'Las ventanillas de ese peaje son: {ventanillas_list}')
    ventanilla_id = int(input("Ingrese el identificador de una de las ventanilla: "))
    if ventanilla_id not in ventanillas_list:
        database.close()
        print('Error buscando ventanilla')
        input('Presione enter para continuar...')
        return

    vehiculo_matricula: str = input("Ingrese matricula del vehículo: ")
    try:
        vehiculo = Vehiculo.get(Vehiculo.vehiculo_matricula == vehiculo_matricula)
    except Exception as e:
        database.close()
        print('Error buscando vehiculo')
        print(e)
        input('Presione enter para continuar...')
        return

    tarifa: str = input("ingrese tarifa: ")

    try:
        bonificacion = mongo_database['Bonificaciones'].find_one({'cuenta': cuenta.cuenta_id, 'peaje': peaje.peaje_id})
        descuento = int(bonificacion['descuento'].removesuffix('%')) if bonificacion else 0
        descuento = 1 - descuento/100
        new_debito: Debito = Debito.create(
            debito_fecha_y_hora=datetime.now(),
            debito_cuenta=cuenta,
            debito_peaje=peaje,
            debito_vehiculo=vehiculo,
            debito_ventanilla=ventanilla_id,
            debito_monto=int(tarifa)*descuento
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


def get_cuenta_y_peaje(database, desea) -> (Cuenta, Peaje):
    propietario = None

    if desea == 'p':
        dni: str = input('Ingrese el dni de la persona: ')
        try:
            persona = Persona.get(Persona.persona_dni == dni)
            propietario = Propietario.get(
                Propietario.propietario_persona == persona)
        except Exception as e:
            database.close()
            print('Error buscando persona')
            print(e)
            input('Presione enter para continuar...')
            return
    else:
        rut: str = input('Ingrese el rut de la empresa: ')
        try:
            empresa = Empresa.get(Empresa.empresa_rut == rut)
            propietario = Propietario.get(
                Propietario.propietario_empresa == empresa)
        except Exception as e:
            database.close()
            print('Error buscando empresa')
            print(e)
            input('Presione enter para continuar...')
            return

    try:
        cuenta = Cuenta.get(Cuenta.cuenta_propietario == propietario)
    except Exception as e:
        database.close()
        print('Error buscando cuenta')
        print(e)
        input('Presione enter para continuar...')
        return

    nombre: str = input("Ingrese el nombre del peaje: ")
    try:
        peaje = Peaje.get(Peaje.peaje_nombre == nombre)
    except Exception as e:
        database.close()
        print('Error buscando peaje')
        print(e)
        input('Presione enter para continuar...')
        return

    return (cuenta, peaje)
