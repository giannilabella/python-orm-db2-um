from src.database import postgres_connect
from src.models.ventanilla import Ventanilla
from src.models.ventanilla import Peaje


def agregar_ventanilla():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    nombre_peaje_vinculado: str = input("Ingrese el nombre del peaje al cual pertenece la ventanilla: ")
    peaje:Peaje = None
    try:
        peaje = Peaje.get(Peaje.peaje_nombre == nombre_peaje_vinculado)
    except Exception as e:
        database.close()
        print('Error buscando peaje')
        print(e)
        input('Presione enter para continuar...')
        return

    rfid_status: str = input("La ventanilla es RFID? (y/n)")

    if rfid_status == "y":
        rfid_status_b:bool = True    
    else:
        rfid_status_b:bool = False 
    
    try:
        new_ventanilla:Ventanilla = Ventanilla.create(
            ventanilla_peaje = peaje,
            ventanilla_es_rfid = rfid_status_b
        )
        peaje.peaje_cantidad_ventanillas += 1
        peaje.save() 
        print(f'ventanilla creada con identificador {new_ventanilla.ventanilla_id}')
        input('Presione enter para continuar...')
        return new_ventanilla
    except Exception as e:
        database.close()
        print('Error creando ventanilla')
        print(e)
        input('Presione enter para continuar...')
        return

def modificar_ventanilla():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return
    
    id_ventanilla: str = input("Ingrese el identificador de la ventanilla (si no lo conoce presione enter): ")
    if id_ventanilla == "":
        try:
            for par in Ventanilla.select():
                print(f"peaje: {par.ventanilla_peaje.peaje_nombre}, identificador de ventanilla: {par.ventanilla_id}, es rfid:{par.ventanilla_es_rfid}")
            
            id_ventanilla: str = input("Ingrese el identificador de la ventanilla (si no lo conoce presione enter): ")
        except Exception as e:
            database.close()
            print('Error buscando peajes y ventanillas')
            print(e)
            input('Presione enter para continuar...')
            return
        
        ventanilla:Ventanilla = None
        try:
            ventanilla = Ventanilla.get(Ventanilla.ventanilla_id == id_ventanilla)
        except Exception as e:
            database.close()
            print('Error buscando ventanilla')
            print(e)
            input('Presione enter para continuar...')
            return

        print(f"el estado rfid de la ventanilla es:{ventanilla.ventanilla_es_rfid}")
        inp = input("Ingrese si es rfid  (y/n), o presione enter para no alterar el estado antiguo: ")

        if inp == "y":
            inp_b:bool = True    
        else:
            inp_b:bool = False 
        
        try:
            if inp != "":
                ventanilla.ventanilla_es_rfid = inp_b
                ventanilla.save()

            print('ventanilla modificada')
            input('Presione enter para continuar...')
            return ventanilla
        except Exception as e:
            database.close()
            print('Error creando ventanilla')
            print(e)
            input('Presione enter para continuar...')
            return


def borrar_ventanilla():
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    id_ventanilla: str = input("Ingrese el identificador de la ventanilla (si no lo conoce presione enter): ")
    if id_ventanilla == "":
        try:
            for par in Ventanilla.select():
                print(f"peaje: {par.ventanilla_peaje.peaje_nombre}, identificador de ventanilla: {par.ventanilla_id}, es rfid:{par.ventanilla_es_rfid}")
            
            id_ventanilla: str = input("Ingrese el identificador de la ventanilla: ")
        except Exception as e:
            database.close()
            print('Error buscando peajes y ventanillas')
            print(e)
            input('Presione enter para continuar...')
            return
        
        ventanilla:Ventanilla = None
        try:
            ventanilla = Ventanilla.get(Ventanilla.ventanilla_id == id_ventanilla)
            ventanilla.delete_instance()
            print('Ventanilla borrada')
            input('Presione enter para continuar...')
            database.close()
            return ventanilla
        except Exception as e:
            database.close()
            print('Error buscando ventanilla')
            print(e)
            input('Presione enter para continuar...')
            return

