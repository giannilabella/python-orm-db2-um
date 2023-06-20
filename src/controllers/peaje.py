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
    telefono: str = input("Ingrese teléfono (13 char): ")
    kilometro: str = input("Ingrese kilómetro: ")
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

    nombre: str = input("Ingrese el nombre del peaje: ")

    try:
        old_peaje = Peaje.get(Peaje.peaje_nombre==nombre)
    except Exception as e:
        database.close()
        print('Error buscando peaje')
        print(e)
        input('Presione enter para continuar...')
        return
    print(f"ruta antigua: {old_peaje.peaje_ruta}")
    new_ruta: str = input("ingrese ruta nueva, o presione enter para no alterar la ruta antigua: ")
    print(f"nombre antiguo: {old_peaje.peaje_nombre}")
    new_nombre: str = input("ingrese nombre nuevo, o presione enter para no alterar el nombre antiguo: ")
    print(f"teléfono antiguo: {old_peaje.peaje_telefono}")
    new_telefono: str = input("ingrese teléfono nuevo, o presione enter para no alterar el teléfono antiguo: ")
    print(f"kilómetro antiguo: {old_peaje.peaje_kilometro}")
    new_kilometro: str = input("ingrese kilómetro nuevo, o presione enter para no alterar el kilómetro antiguo: ")

    try:
        if new_ruta != "":
            old_peaje.peaje_ruta = new_ruta
        if new_nombre != "":
            old_peaje.peaje_nombre = new_nombre
        if new_telefono != "":
            old_peaje.peaje_telefono = new_telefono
        if new_kilometro != "":
            old_peaje.peaje_kilometro = new_kilometro
        old_peaje.save()

        database.close()
        print('Peaje modificado')
        input('Presione enter para continuar...')
        return old_peaje
    except Exception as e:
        database.close()
        print('Error creando peaje')
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

