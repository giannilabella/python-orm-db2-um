def agregar_persona():

    dni:str             = input("ingrese dni (sin puntos ni guion): ")
    nombre_1:str        = input("ingrese primer nombre: ")
    nombre_2:str        = input("ingrese segundo nombre: ")
    direccion:str       = input("ingrese direccion: ")
    apellido_1:str      = input("ingrese primer apellido: ")
    apellido_2:str      = input("ingrese segundo apellido: ")
    mail:str            = input("ingrese e-mail: ")
    celular:str         = input("ingrese celular: ")
    
    hay_persona_asociada:str   = input("tiene personas asociadas (y/n): ")
    hay_persona_asociada       = hay_persona_asociada.lower()

    personas_asociadas:list[str]  = []
    if(hay_persona_asociada in ["y","yes","y/","yes/","si","si/"]):
        tmp:str   = input("indique el numero de personas asociadas: ")
        if (tmp.isdecimal):
            for i in range(int(tmp)):
                personas_asociadas.append(input("ingrese dni de persona asociada :"))
        else:
            input("entrada no valida, toque cualquier tecla para continuar...")
            return
    elif(hay_persona_asociada in ["n","no","n/","no/"]):
        pass
    else:
        input("entrada no valida, toque cualquier tecla para continuar...")
        return

    #tmp:object new Persona(dni,nombre_1,nombre_2,direccion,apellido_1,apellido_2,mail,celular,personas_asociadas)


def agregar_propietario():
    pass

def agregar_cuenta():
    pass

def agregar_vehiculo():
    pass

def agregar_peaje():
    pass

def agregar_bonificacion():
    pass

def modificar_persona():
    pass

def modificar_propietario():
    pass

def modificar_cuenta():
    pass

def modificar_vehiculo():
    pass

def modificar_peaje():
    pass

def modificar_bonificacion():
    pass

def nuevo_deposito():
    pass

def nueva_carga():
    pass

def agregar_tipo_vehiculo():
    pass

def agregar_tarifa():
    pass

def modificar_tipo_de_vehiculo():
    pass

def modificar_tarifa():
    pass
