from src.database import postgres_connect
from src.models.persona import Persona
from src.models.propietario import Propietario


def agregar_persona() -> Persona:
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error conectandose con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    dni: str = input("ingrese dni (sin puntos ni guion): ")
    nombre_1: str = input("ingrese primer nombre: ")
    nombre_2: str = input("ingrese segundo nombre: ")
    direccion: str = input("ingrese dirección: ")
    apellido_1: str = input("ingrese primer apellido: ")
    apellido_2: str = input("ingrese segundo apellido: ")
    mail: str = input("ingrese e-mail: ")
    celular: str = input("ingrese celular: ")

    desea_asociar: str = input("desea asociar a otra persona (y/n): ").lower()
    asociado = None

    if desea_asociar == 'y':
        dni_asociado: str = input("ingrese el dni de la persona: ")
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
