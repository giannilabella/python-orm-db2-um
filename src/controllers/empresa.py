from src.database import postgres_connect
from src.models.empresa import Empresa
from src.models.propietario import Propietario


def agregar_empresa() -> Empresa:
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error conectando con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return
    
    rut:str = input("Ingrese RUT (sin puntos ni guion): ")
    nombre:str = input("Ingrese nombre: ")
    direccion:str = input("Ingrese dirección: ")

    try:
        new_empresa:Empresa = Empresa.create(
            empresa_rut         =   rut,
            empresa_nombre      =   nombre,
            empresa_direccion   =   direccion
        )
        Propietario.create(
            propietario_persona_id = None,
            propietario_empresa_id = new_empresa
        )
        database.close()
        print('Empresa creada')
        input('Presione enter para continuar...')
        return new_empresa
    except Exception as e:
        database.close()
        print('Error creando empresa')
        print(e)
        input('Presione enter para continuar...')
        return
    

def modificar_empresa()->Empresa:
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error conectando con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return
    
    rut:str = input("Ingrese RUT (sin puntos ni guion): ")
    
    old_empresa:Empresa = None
    try:
        old_empresa = Empresa.get(Empresa.empresa_rut == rut)
    except Exception as e:
        database.close()
        print('Error buscando empresa')
        print(e)
        input('Presione enter para continuar...')
        return

    print(f"rut antiguo: {old_empresa.empresa_rut}")
    rut_nuevo: str = input("ingrese rut nuevo, o presione enter para no alterar el rut antiguo: ")

    print(f"nombre antiguo: {old_empresa.empresa_nombre}")
    nombre_nuevo: str = input("ingrese nombre nuevo, o presione enter para no alterar el nombre antiguo: ")

    print(f"dirección antigua: {old_empresa.empresa_direccion}")
    direccion_nueva: str = input("ingrese dirección nueva, o presione enter para no alterar la dirección antigua: ")

    try:
        if rut_nuevo != "":
            old_empresa.empresa_rut = rut_nuevo

        if nombre_nuevo != "":
            old_empresa.empresa_nombre = nombre_nuevo

        if direccion_nueva != "":
            old_empresa.empresa_direccion = direccion_nueva
        
        old_empresa.save()

        print('Modificaciones guardadas')
        input('Presione enter para continuar...')
        database.close()
        return old_empresa
    except Exception as e:
        database.close()
        print('Error modificando empresa')
        print(e)
        input('Presione enter para continuar...')
        return
                
def borrar_empresa()->Empresa:
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error conectando con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return
    
    rut:str = input("Ingrese RUT (sin puntos ni guion): ")
    
    old_empresa:Empresa = None
    old_propietario:Propietario = None
    try:
        old_empresa = Empresa.get(Empresa.empresa_rut == rut)
        old_propietario = Propietario.get(Propietario.propietario_empresa_id == old_empresa)
    except Exception as e:
        print('Error buscando empresa')
        print(e)
        input('Presione enter para continuar...')
        database.close()
        return
    
    try:
        old_propietario.delete_instance()
        old_empresa.delete_instance()
        print('Empresa borrada')
        input('Presione enter para continuar...')
        database.close()
        return old_empresa
    except Exception as e:
        database.close()
        print('Error borrando empresa')
        print(e)
        input('Presione enter para continuar...')
        return




#    print("A") if a > b else print("B")