from datetime import date
from src.database import postgres_connect
from src.models.cuenta import Cuenta
from src.models.persona import Persona
from src.models.empresa import Empresa
from src.models.propietario import Propietario


def agregar_cuenta():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    desea_crear: str = input('Desea crear para Persona o Empresa (p/e): ').lower()
    propietario = None

    if desea_crear == 'p':
        dni: str = input('Ingrese el dni de la persona: ')
        try:
            persona = Persona.get(Persona.persona_dni == dni)
            propietario = Propietario.get(Propietario.propietario_persona_id == persona)
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
            propietario = Propietario.get(Propietario.propietario_empresa_id == empresa)
        except Exception as e:
            database.close()
            print('Error buscando empresa')
            print(e)
            input('Presione enter para continuar...')
            return

    try:
        Cuenta.create(
            cuenta_creacion=date.today(),
            cuenta_saldo=0,
            cuenta_propietario_id=propietario
        )
        database.close()
        print('Cuenta creada')
        input('Presione enter para continuar...')
        return
    except Exception as e:
        database.close()
        print('Error creando cuenta')
        print(e)
        input('Presione enter para continuar...')
        return


def modificar_cuenta():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    desea_modificar: str = input('Desea modificar cuenta de Persona o Empresa (p/e): ').lower()
    propietario = None

    if desea_modificar == 'p':
        dni: str = input('Ingrese el dni de la persona: ')
        try:
            persona = Persona.get(Persona.persona_dni == dni)
            propietario = Propietario.get(Propietario.propietario_persona_id == persona)
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
            propietario = Propietario.get(Propietario.propietario_empresa_id == empresa)
        except Exception as e:
            database.close()
            print('Error buscando empresa')
            print(e)
            input('Presione enter para continuar...')
            return

    cuenta = None
    try:
        cuenta = Cuenta.get(Cuenta.cuenta_propietario_id == propietario)
    except Exception as e:
        database.close()
        print('Error buscando cuenta')
        print(e)
        input('Presione enter para continuar...')
        return

    print('Deje nuevo valor vacio para mantener valor actual')
    print(f'Saldo actual: {cuenta.cuenta_saldo}')
    saldo: str = input('Ingrese nuevo saldo: ')


    try:
        Cuenta.update(
            cuenta_saldo=saldo if saldo != '' else cuenta.cuenta_saldo,
        ).where(Cuenta.cuenta_propietario_id == propietario).execute()
        database.close()
        print('Cuenta modificada')
        input('Presione enter para continuar...')
        return
    except Exception as e:
        database.close()
        print('Error modificando cuenta')
        print(e)
        input('Presione enter para continuar...')
        return


def borrar_cuenta():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    desea_borrar: str = input('Desea borrar cuenta de Persona o Empresa (p/e): ').lower()
    propietario = None

    if desea_borrar == 'p':
        dni: str = input('Ingrese el dni de la persona: ')
        try:
            persona = Persona.get(Persona.persona_dni == dni)
            propietario = Propietario.get(Propietario.propietario_persona_id == persona)
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
            propietario = Propietario.get(Propietario.propietario_empresa_id == empresa)
        except Exception as e:
            database.close()
            print('Error buscando empresa')
            print(e)
            input('Presione enter para continuar...')
            return

    try:
        Cuenta.delete().where(Cuenta.cuenta_propietario_id == propietario).execute()
        database.close()
        print('Cuenta borrada')
        input('Presione enter para continuar...')
        return
    except Exception as e:
        database.close()
        print('Error borrando cuenta')
        print(e)
        input('Presione enter para continuar...')
        return
