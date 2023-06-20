from datetime import date

from src.database import psycopg2_connect, postgres_connect

from src.models.cuenta import Cuenta
from src.models.persona import Persona
from src.models.empresa import Empresa
from src.models.propietario import Propietario


def listar_cuentas():
    try:
        connection = psycopg2_connect()
    except Exception as e:
        print('Error al conectarse con la base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    select
                        persona_id,
                        persona_dni,
                        empresa_rut,
                        cuenta_saldo,
                        cuenta_creacion,
                        string_agg(vehiculo_matricula, ', ') as vehiculos
                    from
                        cuenta
                    inner join propietario on
                        (cuenta_propietario_id = propietario_id)
                    left outer join persona on
                        (propietario_persona_id = persona_id)
                    left outer join empresa on
                        (propietario_empresa_id = empresa_id)
                    left outer join propietariovehiculo on
                        (propietario_id = propietario_vehiculo_propietario_id)
                    left outer join vehiculo on
                        (propietario_vehiculo_vehiculo_id = vehiculo_id)
                    group by
                        persona_id, persona_dni, empresa_rut, cuenta_saldo, cuenta_creacion;
                """)
            except Exception as e:
                print('Error al listar cuentas')
                print(e)
                input('Presione enter para continuar...')
                return

            for (persona_id, dni, rut, saldo, creacion, vehiculos) in cursor.fetchall():
                if dni is None:
                    print(f'Cuenta de la empresa de RUT {rut}, creada en {creacion}, tiene ${saldo} de saldo y las matriculas de sus vehiculos asociados son: {vehiculos}')
                else:
                    cursor.execute("""
                        select
                            persona_dni,
                            string_agg(vehiculo_matricula, ', ') as vehiculos
                        from
                            propietario
                        inner join persona on
                            (propietario_persona_id = persona_id) and
                            (persona_asociado_id = {})
                        left outer join propietariovehiculo on
                            (propietario_id = propietario_vehiculo_propietario_id)
                        left outer join vehiculo on
                            (propietario_vehiculo_vehiculo_id = vehiculo_id)
                        group by
                            persona_dni;
                    """.format(persona_id))
                    result = cursor.fetchone()
                    vehiculos += ', ' + result[1] if result else ''
                    print(f'Cuenta de la persona de DNI {dni}, creada en {creacion}, tiene ${saldo} de saldo y las matriculas de sus vehiculos asociados son: {vehiculos}')

    connection.close()


def agregar_cuenta():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    desea_crear: str = input(
        'Desea crear para Persona o Empresa (p/e): ').lower()
    propietario = None

    if desea_crear == 'p':
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
        Cuenta.create(
            cuenta_creacion=date.today(),
            cuenta_saldo=0,
            cuenta_propietario=propietario
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

    desea_modificar: str = input(
        'Desea modificar cuenta de Persona o Empresa (p/e): ').lower()
    propietario = None

    if desea_modificar == 'p':
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

    cuenta = None
    try:
        cuenta = Cuenta.get(Cuenta.cuenta_propietario == propietario)
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
        ).where(Cuenta.cuenta_propietario == propietario).execute()
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

    desea_borrar: str = input(
        'Desea borrar cuenta de Persona o Empresa (p/e): ').lower()
    propietario = None

    if desea_borrar == 'p':
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
        Cuenta.delete().where(Cuenta.cuenta_propietario == propietario).execute()
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
