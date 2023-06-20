from src.database import postgres_connect
from src.models.vehiculo import Vehiculo
from src.models.tipo_vehiculo import TipoVehiculo
from src.models.persona import Persona
from src.models.empresa import Empresa
from src.models.propietario import Propietario
from src.models.propietario_vehiculo import PropietarioVehiculo


def agregar_vehiculo():
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

    matricula = input('Ingrese matricula: ')
    rfid = input('Ingrese id rfid: ')
    marca = input('Ingrese marca: ')
    color = input('Ingrese color: ')
    modelo = input('Ingrese modelo: ')

    tipos = TipoVehiculo.select()
    tipos_list = list(map(lambda t: t.tipo_vehiculo_tipo, tipos))
    print(f'Los tipos definidos son: {tipos_list}')
    tipo: str = input('Ingrese uno de los definidos o uno nuevo: ')

    if tipo in tipos_list:
        tipo = tipos[tipos_list.index(tipo)]
    else:
        try:
            tipo = TipoVehiculo.create(
                tipo_vehiculo_tipo=tipo
            )
        except Exception as e:
            database.close()
            print('Error creando tipo vehiculo')
            print(e)
            input('Presione enter para continuar...')
            return

    try:
        nuevo_vehiculo = Vehiculo.create(
            vehiculo_id_rfid=rfid,
            vehiculo_id_tipo=tipo,
            vehiculo_marca=marca,
            vehiculo_color=color,
            vehiculo_modelo=modelo,
            vehiculo_matricula=matricula,
        )
        PropietarioVehiculo.create(
            id_vehiculo=nuevo_vehiculo,
            id_propietario=propietario,
        )
        database.close()
        print('Vehiculo creado')
        input('Presione enter para continuar...')
        return
    except Exception as e:
        database.close()
        print('Error creando vehiculo')
        print(e)
        input('Presione enter para continuar...')
        return


def modificar_vehiculo():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    matricula = input('Ingrese matricula: ')
    vehiculo = None
    try:
        vehiculo = Vehiculo.get(Vehiculo.vehiculo_matricula == matricula)
    except Exception as e:
        database.close()
        print('Error buscando vehiculo')
        print(e)
        input('Presione enter para continuar...')
        return

    print('Deje nuevo valor vacio para mantener valor actual')
    print(f'Id rfid actual: {vehiculo.vehiculo_id_rfid}')
    rfid = input('Ingrese nuevo id rfid: ')
    print('Marca actual: ' + vehiculo.vehiculo_marca)
    marca = input('Ingrese marca: ')
    print('Color actual: ' + vehiculo.vehiculo_color)
    color = input('Ingrese color: ')
    print('Modelo actual: ' + vehiculo.vehiculo_modelo)
    modelo = input('Ingrese modelo: ')

    tipos = TipoVehiculo.select()
    tipos_list = list(map(lambda t: t.tipo_vehiculo_tipo, tipos))
    print(f'Los tipos definidos son: {tipos_list}')
    print('Tipo actual: ' + vehiculo.vehiculo_id_tipo.tipo_vehiculo_tipo)
    tipo = input('Ingrese nuevo tipo: ')
    if tipo in tipos_list:
        tipo = tipos[tipos_list.index(tipo)]
    else:
        try:
            tipo = TipoVehiculo.create(
                tipo_vehiculo_tipo=tipo
            )
        except Exception as e:
            database.close()
            print('Error creando tipo vehiculo')
            print(e)
            input('Presione enter para continuar...')
            return

    # propietarios = PropietarioVehiculo.select().where(PropietarioVehiculo.id_vehiculo == vehiculo)
    # prop_list = list(map(lambda p: PropietarioVehiculo.id_propietar, tipos))
    # print(f'Los tipos definidos son: {tipos_list}')
    # print('Tipo actual: ' + vehiculo.vehiculo_id_tipo.tipo_vehiculo_tipo)
    # tipo = input('Ingrese nuevo tipo: ')
    # if tipo in tipos_list:
    #     tipo = tipos[tipos_list.index(tipo)]
    # else:
    #     try:
    #         tipo = TipoVehiculo.create(
    #             tipo_vehiculo_tipo=tipo
    #         )
    #     except Exception as e:
    #         database.close()
    #         print('Error creando tipo vehiculo')
    #         print(e)
    #         input('Presione enter para continuar...')
    #         return

    try:
        Vehiculo.update(
            vehiculo_id_rfid=rfid if rfid != '' else vehiculo.vehiculo_id_rfid,
            vehiculo_id_tipo=tipo,
            vehiculo_marca=marca if marca != '' else vehiculo.vehiculo_marca,
            vehiculo_color=color if color != '' else vehiculo.vehiculo_color,
            vehiculo_modelo=modelo if modelo != '' else vehiculo.vehiculo_modelo,
        ).where(Vehiculo.vehiculo_matricula == matricula).execute()
        database.close()
        print('Vehiculo modificado')
        input('Presione enter para continuar...')
        return
    except Exception as e:
        database.close()
        print('Error modificando vehiculo')
        print(e)
        input('Presione enter para continuar...')
        return


def borrar_vehiculo():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    matricula = input('Ingrese matricula: ')

    try:
        Vehiculo.delete().where(Vehiculo.vehiculo_matricula == matricula).execute()
        database.close()
        print('Vehiculo borrado')
        input('Presione enter para continuar...')
        return
    except Exception as e:
        database.close()
        print('Error borrando vehiculo')
        print(e)
        input('Presione enter para continuar...')
        return
