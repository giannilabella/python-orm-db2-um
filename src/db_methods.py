def agregar_persona():
    fail = False
    while(fail != True):
        persona_dni:str             = input("ingrese dni (sin puntos ni guion): ")
        persona_nombre_1:str        = input("ingrese primer nombre: ")
        persona_nombre_2:str        = input("ingrese segundo nombre: ")
        persona_direccion:str       = input("ingrese direccion: ")
        persona_apellido_1:str      = input("ingrese primer apellido: ")
        persona_apellido_2:str      = input("ingrese segundo apellido: ")
        persona_mail:str            = input("ingrese e-mail: ")
        persona_celular:str         = input("ingrese celular: ")
        
        hay_persona_asociada:str   = input("tiene personas asociadas (y/n): ")
        
        if(hay_persona_asociada in ["y","yes","y/","yes/","si","si/"]):
            pass
        elif(hay_persona_asociada in ["n","no","n/","no/"]):
            pass
        else:
            fail = True


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
