from peeweeClasses import *

def agregar_persona():

    dni:str             = input("ingrese dni (sin puntos ni guion): ")
    nombre_1:str        = input("ingrese primer nombre: ")
    nombre_2:str        = input("ingrese segundo nombre: ")
    direccion:str       = input("ingrese direccion: ")
    apellido_1:str      = input("ingrese primer apellido: ")
    apellido_2:str      = input("ingrese segundo apellido: ")
    mail:str            = input("ingrese e-mail: ")
    celular:str         = input("ingrese celular: ")
    
    asociad0:str   = input("ingrese dni de persona asociada")
    try:
        new_persona = Persona.create(
            persona_dni      =dni,
            persona_nombre_1  =nombre_1,
            persona_nombre_2=nombre_2,
            persona_direccion=direccion,
            persona_apellido_1=apellido_1,
            persona_apellido_2=apellido_2,
            persona_mail=mail,
            persona_celular =    celular,
            persona_dni_asociado=1,)
    except Exception:
        input("dato no valido ingresado para algún dato pedido")
        return
    


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
