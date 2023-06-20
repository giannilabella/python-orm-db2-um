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

    desea_modificar: str = input(
        'Desea bonificar cuenta de Persona o Empresa (p/e): ').lower()
    propietario = None

    if desea_modificar == 'p':
        dni: str = input('Ingrese el dni de la persona: ')
        try:
            persona = Persona.get(Persona.persona_dni == dni)
            propietario = Propietario.get(
                Propietario.propietario_persona == persona)
        except Exception as e:
            postgres_database.close()
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
            postgres_database.close()
            print('Error buscando empresa')
            print(e)
            input('Presione enter para continuar...')
            return

    cuenta = None
    try:
        cuenta = Cuenta.get(Cuenta.cuenta_propietario == propietario)
    except Exception as e:
        postgres_database.close()
        print('Error buscando cuenta')
        print(e)
        input('Presione enter para continuar...')
        return

    nombre: str = input("Ingrese el nombre del peaje: ")

    try:
        peaje = Peaje.get(Peaje.peaje_nombre == nombre)
    except Exception as e:
        postgres_database.close()
        print('Error buscando peaje')
        print(e)
        input('Presione enter para continuar...')
        return

    motivo = input("Ingrese motivo: ")
    descuento = input("Ingrese descuento (xx%): ")
    fecha_otorgo = input("Ingrese fecha otorgo: ")
    fecha_renovacion = input("Ingrese fecha renovacion: ")

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
        database = mongodb_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return


def borrar_bonificacion():
    try:
        database = mongodb_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return
