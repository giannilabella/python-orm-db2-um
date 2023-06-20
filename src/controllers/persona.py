from src.database import postgres_connect
from src.models.persona import Persona
from src.models.propietario import Propietario


def agregar_persona() -> Persona:
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    dni: str = input('Ingrese dni (sin puntos ni guion): ')
    nombre_1: str = input('Ingrese primer nombre: ')
    nombre_2: str = input('Ingrese segundo nombre: ')
    direccion: str = input('Ingrese dirección: ')
    apellido_1: str = input('Ingrese primer apellido: ')
    apellido_2: str = input('Ingrese segundo apellido: ')
    mail: str = input('Ingrese e-mail: ')
    celular: str = input('Ingrese celular: ')

    desea_asociar: str = input('Desea asociar a otra persona (y/n): ').lower()
    asociado = None

    if desea_asociar == 'y':
        dni_asociado: str = input('Ingrese el dni de la persona: ')
        try:
            asociado = Persona.get(Persona.persona_dni == dni_asociado)
        except Exception as e:
            database.close()
            print('Error buscando persona')
            print(e)
            input('Presione enter para continuar...')
            return

    try:
        nueva_persona: Persona = Persona.create(
            persona_dni=dni,
            persona_nombre_1=nombre_1,
            persona_nombre_2=nombre_2,
            persona_direccion=direccion,
            persona_apellido_1=apellido_1,
            persona_apellido_2=apellido_2,
            persona_mail=mail,
            persona_celular=celular,
            persona_id_asociado=asociado,
        )
        Propietario.create(
            propietario_persona_id=nueva_persona.persona_id,
            propietario_empresa_id=None
        )
        database.close()
        print('Persona creada')
        input('Presione enter para continuar...')
        return nueva_persona
    except Exception as e:
        database.close()
        print('Error creando persona')
        print(e)
        input('Presione enter para continuar...')
        return


def modificar_persona():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    dni: str = input('Ingrese dni (sin puntos ni guion): ')
    persona: Persona = None
    try:
        persona = Persona.get(Persona.persona_dni == dni)
    except Exception as e:
        database.close()
        print('Error buscando persona')
        print(e)
        input('Presione enter para continuar...')
        return

    print('Deje nuevo valor vacio para mantener valor actual')
    print('Primer nombre actual: ' + persona.persona_nombre_1)
    nombre_1: str = input('Ingrese nuevo primer nombre: ')
    print('Segundo nombre actual: ' + persona.persona_nombre_2)
    nombre_2: str = input('Ingrese nuevo segundo nombre: ')
    print('Direccion actual: ' + persona.persona_direccion)
    direccion: str = input('Ingrese nueva dirección: ')
    print('Primer apellido actual: ' + persona.persona_apellido_1)
    apellido_1: str = input('Ingrese nuevo primer apellido: ')
    print('Segundo apellido actual: ' + persona.persona_apellido_1)
    apellido_2: str = input('Ingrese nuevo segundo apellido: ')
    print('Email actual: ' + persona.persona_mail)
    mail: str = input('Ingrese nuevo e-mail: ')
    print('Celular actual: ' + persona.persona_celular)
    celular: str = input('Ingrese nuevo celular: ')
    print('DNI asociado actual: ' + persona.persona_id_asociado.persona_dni if persona.persona_id_asociado else 'Sin asociado')
    dni_asociado: str = input('Ingrese DNI de nuevo asociado: ')

    if dni_asociado:
        try:
            asociado = Persona.get(Persona.persona_dni == dni_asociado)
        except Exception as e:
            database.close()
            print('Error buscando persona')
            print(e)
            input('Presione enter para continuar...')
            return

    try:
        Persona.update(
            persona_nombre_1=nombre_1 if nombre_1 != '' else persona.persona_nombre_1,
            persona_nombre_2=nombre_2 if nombre_2 != '' else persona.persona_nombre_2,
            persona_direccion=direccion if direccion != '' else persona.persona_direccion,
            persona_apellido_1=apellido_1 if apellido_1 != '' else persona.persona_apellido_1,
            persona_apellido_2=apellido_2 if apellido_2 != '' else persona.persona_apellido_2,
            persona_mail=mail if mail != '' else persona.persona_mail,
            persona_celular=celular if celular != '' else persona.persona_celular,
            persona_id_asociado=asociado if dni_asociado != '' else persona.persona_id_asociado,
        ).where(Persona.persona_id == persona.persona_id).execute()
        database.close()
        print('Persona modificada')
        input('Presione enter para continuar...')
    except Exception as e:
        database.close()
        print('Error modificando persona')
        print(e)
        input('Presione enter para continuar...')
        return


def borrar_persona():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    dni: str = input('Ingrese dni (sin puntos ni guion): ')
    persona: Persona = None
    try:
        persona = Persona.get(Persona.persona_dni == dni)
    except Exception as e:
        database.close()
        print('Error buscando persona')
        print(e)
        input('Presione enter para continuar...')
        return

    try:
        Persona.delete().where(Persona.persona_id == persona.persona_id).execute()
        database.close()
        print('Persona borrada')
        input('Presione enter para continuar...')
    except Exception as e:
        database.close()
        print('Error borrando persona')
        print(e)
        input('Presione enter para continuar...')
        return
