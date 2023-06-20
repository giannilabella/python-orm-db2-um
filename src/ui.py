import os
import platform
from src.controllers.cuenta import *
from src.controllers.empresa import *
from src.controllers.peaje import *
from src.controllers.persona import *
from src.controllers.vehiculo import *
from src.controllers.ventanilla import *
from src.controllers.bonificacion import *
from src.controllers.debito import *
from src.controllers.carga import *

def clear_console():
    match (platform.system()):
        case "Linux":
            os.system("clear")
        case "Windows":
            os.system("cls")
        case "MacOS":
            os.system("clear")
        case _:
            pass

def displayMenu(menu_select)->None:
    clear_console()    
    match (menu_select):
        case "menu_de_inicio":
            print(
                "******************************************Welcome User********************************************\n"+
                "1- Consultar Datos\n"+
                "2- Agregar Datos \n"+
                "3- Modificar Datos \n"+
                "4- Borrar Datos \n"+
                "\n\n\n\n\n**************************************************************************************************\n"
                )
            input_control("menu_de_inicio")
        case "menu_de_agregar":
            print(
                "*****Agregar Datos******************************************************************************\n"+
                "1- Agregar Persona              7- Agregar Bonificacion \n"+
                "2- Agregar Empresa              8- Agregar Debito       \n"+
                "3- Agregar Cuenta               9- Agregar Carga        \n"+
                "4- Agregar Vehículo             \n"+
                "5- Agregar Peaje                \n"+
                "6- Agregar ventanilla           \n\n"+
                "--------------------------------------------------------------------------------------------------\n"+
                "0- retroceder  |\n"+
                "**************************************************************************************************\n"
                )
            input_control("menu_de_agregar")
        
        case "menu_de_modificacion":
            print(
                "*****Modificar Datos******************************************************************************\n"+
                "1- Modificar Persona              7- Modificar Bonificación\n"+
                "2- Modificar Empresa              \n"+
                "3- Modificar Cuenta               \n"+
                "4- Modificar Vehículo             \n"+
                "5- Modificar Peaje                \n"+
                "6- Modificar ventanilla           \n\n"+
                "--------------------------------------------------------------------------------------------------\n"+
                "0- retroceder  |\n"+
                "**************************************************************************************************\n"
                )
            input_control("menu_de_modificacion")
        case "menu_de_borrar":
            print(
                "*****Borrar Datos******************************************************************************\n"+
                "1- Borrar Persona              7- Borrar Bonificación\n"+
                "2- Borrar Empresa              \n"+
                "3- Borrar Cuenta               \n"+
                "4- Borrar Vehículo             \n"+
                "5- Borrar Peaje                \n"+
                "6- Borrar ventanilla           \n\n"+
                "--------------------------------------------------------------------------------------------------\n"+
                "0- retroceder  |\n"+
                "**************************************************************************************************\n"
                )
            input_control("menu_de_borrar")    
        case "menu_de_consulta":
            print(
                "*****Consultar Datos******************************************************************************\n"+
                "1- Listado de propietarios y sus vehículos\n"+
                "2- Listado de cuentas con su titular y sus vehículos asociados\n\n\n\n\n"+
                "--------------------------------------------------------------------------------------------------\n"+
                "0- retroceder  |\n"+
                "\n**************************************************************************************************\n"
                )
            input_control("menu_de_consulta")

def input_control(input_set)->None:
    match (input_set):
        case "menu_de_inicio":
            inp:str = input("Ingrese el numero que corresponda a la acción que desea tomar: ")
            match(inp):    
                case "1":
                    displayMenu("menu_de_consulta")
                case "2":
                    displayMenu("menu_de_agregar")
                case "3":
                    displayMenu("menu_de_modificacion")
                case "4":
                    displayMenu("menu_de_borrar")
                case _:
                    input("Entrada no valida,presione enter para continuar")

        case "menu_de_agregar":
            inp:str = input("Ingrese el numero que corresponda a la acción que desea tomar: ")
            match(inp):
                case "0":
                    displayMenu("menu_de_inicio")
                case "1":
                    agregar_persona()
                case "2":
                    agregar_empresa()
                case "3":
                    agregar_cuenta()
                case "4":
                    agregar_vehiculo()
                case "5":
                    agregar_peaje()
                case "6":
                    agregar_ventanilla()
                case "7":
                    agregar_bonificacion()
                case "8":
                    agregar_debito()
                case "9":
                    agregar_carga()
                case _:
                    input("Entrada no valida,presione enter para continuar")
        
        case "menu_de_consulta":
            inp:str = input("Ingrese el numero que corresponda a la acción que desea tomar: ")
            match (inp):
                case "0":
                    displayMenu("menu_de_inicio")
                case "1":
                    Listado_de_propietarios_y_sus_vehículos()
                case "2":
                    Listado_de_cuentas_con_su_titular_y_sus_vehículos_asociados()
                case _:
                    input("Entrada no valida,presione enter para continuar")
        
        case "menu_de_borrar":
            inp:str = input("Ingrese el numero que corresponda a la acción que desea tomar: ")
            match (inp):
                case "0":
                    displayMenu("menu_de_inicio")
                case "1":
                    borrar_persona()
                case "2":
                    borrar_empresa()
                case "3":
                    borrar_cuenta()
                case "4":
                    borrar_vehiculo()
                case "5":
                    borrar_peaje()
                case "6":
                    borrar_ventanilla()
                case "7":
                    borrar_bonificacion()
        case "menu_de_modificacion":
            inp:str = input("Ingrese el numero que corresponda a la acción que desea tomar: ")
            match (inp):
                case "0":
                    displayMenu("menu_de_inicio")
                case "1":
                    modificar_persona()
                case "2":
                    modificar_empresa()
                case "3":
                    modificar_cuenta()
                case "4":
                    modificar_vehiculo()
                case "5":
                    modificar_peaje()
                case "6":
                    modificar_ventanilla()
                case "7":
                    modificar_bonificacion()

    displayMenu("menu_de_inicio")


if __name__ == "__main__":
    displayMenu("menu_de_inicio")


