from src.database import postgres_connect
from src.models.peaje import Peaje


def agregar_peaje() -> Peaje:
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    ruta: str = input("Ingrese ruta: ")
    nombre: str = input("Ingrese nombre: ")
    telefono: str = input("Ingrese telefono: ")
    kilometro: str = input("Ingrese kilometro: ")
    cantidad_ventanillas:int = 0

    try:
        new_peaje:Peaje = Peaje.create(
            peaje_ruta = ruta,
            peaje_nombre = nombre,
            peaje_telefono = telefono,
            peaje_kilometro = kilometro,
            peaje_cantidad_ventanillas = cantidad_ventanillas
        )
        database.close()
        print('Peaje creado')
        input('Presione enter para continuar...')
        return new_peaje
    except Exception as e:
        database.close()
        print('Error creando peaje')
        print(e)
        input('Presione enter para continuar...')
        return
    

def modificar_peaje():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return


def borrar_peaje():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

