from src.database import mongodb_connect, postgres_connect

from src.models.cuenta import Cuenta
from src.models.propietario import Propietario
from src.models.persona import Persona
from src.models.empresa import Empresa
from src.models.peaje import Peaje


def agregar_bonificacion():
    try:
        mongo_database = mongodb_connect()
        postgres_database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    desea_bonificar: str = input(
        'Desea bonificar cuenta de Persona o Empresa (p/e): ').lower()
    (cuenta, peaje) = get_cuenta_y_peaje(postgres_database, desea_bonificar)

    motivo = input("Ingrese motivo: ")
    descuento = input("Ingrese descuento (xx%): ")
    fecha_otorgo = input("Ingrese fecha otorgo (yyyy-mm-dd): ")
    fecha_renovacion = input("Ingrese fecha renovacion (yyyy-mm-dd): ")

    try:
        mongo_database['Bonificaciones'].insert_one({
            "motivo": motivo,
            "descuento": descuento,
            "fecha_otorgo": fecha_otorgo,
            "fecha_renovacion": fecha_renovacion,
            "peaje": peaje.peaje_id,
            "cuenta": cuenta.cuenta_id,
        })
        postgres_database.close()
        print('Bonificacion creada')
        input('Presione enter para continuar...')
        return
    except Exception as e:
        postgres_database.close()
        print('Error creando bonificacion')
        print(e)
        input('Presione enter para continuar...')
        return


def modificar_bonificacion():
    try:
        mongo_database = mongodb_connect()
        postgres_database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    desea_modificar: str = input(
        'Desea modificar bonificacion de cuenta de Persona o Empresa (p/e): ').lower()
    (cuenta, peaje) = get_cuenta_y_peaje(postgres_database, desea_modificar)

    fecha_otorgo = input("Ingrese fecha otorgo (yyyy-mm-dd): ")
    query = {
        "fecha_otorgo": fecha_otorgo,
        "peaje": peaje.peaje_id,
        "cuenta": cuenta.cuenta_id,
    }

    try:
        bonificacion = mongo_database['Bonificaciones'].find(query)[0]
    except Exception as e:
        postgres_database.close()
        print('Error buscando bonificacion')
        print(e)
        input('Presione enter para continuar...')
        return

    print('Deje nuevo valor vacio para mantener valor actual')
    print('Motivo actual: ' + bonificacion['motivo'])
    motivo = input("Ingrese nuevo motivo: ")
    print('Descuento actual: ' + bonificacion['descuento'])
    descuento = input("Ingrese neuvo descuento (xx%): ")
    print('Fecha renovacion actual (yyyy-mm-dd): ' + bonificacion['fecha_renovacion'])
    fecha_renovacion = input("Ingrese nuevo fecha renovacion: ")

    try:
        mongo_database['Bonificaciones'].update_one(query, {'$set': {
            "motivo": motivo if motivo != '' else bonificacion['motivo'],
            "descuento": descuento if descuento != '' else bonificacion['descuento'],
            "fecha_renovacion": fecha_renovacion if fecha_renovacion != '' else bonificacion['fecha_renovacion'],
        }})
        postgres_database.close()
        print('Bonificacion modificada')
        input('Presione enter para continuar...')
        return
    except Exception as e:
        postgres_database.close()
        print('Error modificando bonificacion')
        print(e)
        input('Presione enter para continuar...')
        return


def borrar_bonificacion():
    try:
        mongo_database = mongodb_connect()
        postgres_database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    desea_modificar: str = input(
        'Desea bonificacion de cuenta de Persona o Empresa (p/e): ').lower()
    (cuenta, peaje) = get_cuenta_y_peaje(postgres_database, desea_modificar)

    fecha_otorgo = input("Ingrese fecha otorgo (yyyy-mm-dd): ")

    try:
        mongo_database['Bonificaciones'].delete_one({
            "fecha_otorgo": fecha_otorgo,
            "peaje": peaje.peaje_id,
            "cuenta": cuenta.cuenta_id,
        })
        postgres_database.close()
        print('Bonificacion borrada')
        input('Presione enter para continuar...')
        return
    except Exception as e:
        postgres_database.close()
        print('Error borrando bonificacion')
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
