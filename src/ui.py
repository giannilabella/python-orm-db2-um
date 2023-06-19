import os
import platform
from src.db_methods import *

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
                "2- Modificar Datos Preexistentes\n\n\n\n\n\n\n"+
                "\n**************************************************************************************************\n"
                )
            input_control("menu_de_inicio")
        case "menu_de_modificacion":
            print(
                "*****Modificar Datos******************************************************************************\n"+
                "1- Agregar Persona              7- Modificar Persona           13- Nuevo debito\n"+
                "2- Agregar Propietario          8- Modificar Propietario       14- Nueva carga\n"+
                "3- Agregar Cuenta               9- Modificar Cuenta            15- Agregar tipo de vehículo\n"+
                "4- Agregar Vehículo             10- Modificar Vehículo         16- Agregar tarifa\n"+
                "5- Agregar Peaje                11- Modificar Peaje            17- Modificar tipo de vehículo\n"+
                "6- Agregar Bonificación         12- Modificar Bonificación     18- Modificar tarifa\n\n"+
                "--------------------------------------------------------------------------------------------------\n"+
                "0- retroceder  |\n"+
                "**************************************************************************************************\n"
                )
            input_control("menu_de_modificacion")
        case "menu_de_consulta":
            print(
                "*****Consultar Datos******************************************************************************\n"+
                "1- Listado de propietarios y sus vehículos\n"+
                "2- Listado de cuentas con su titular y sus vehículos asociados\n\n\n\n\n"+
                "--------------------------------------------------------------------------------------------------\n"+
                "0- retroceder  |\n"+
                "\n**************************************************************************************************\n"
                )
            input_control("menu_de_modificacion")

def input_control(input_set)->None:
    match (input_set):
        case "menu_de_inicio":
            inp:str = input("Ingrese el numero que corresponda a la acción que desea tomar: ")
            match(inp):    
                case "1":
                    displayMenu("menu_de_consulta")
                case "2":
                    displayMenu("menu_de_modificacion")
                case _:
                    input("Entrada no valida,presione enter para continuar")

        case "menu_de_modificacion":
            inp:str = input("Ingrese el numero que corresponda a la acción que desea tomar: ")
            match(inp):
                case "0":
                    displayMenu("menu_de_inicio")
                case "1":
                    agregar_persona()
                case "2":
                    agregar_propietario()
                case "3":
                    agregar_cuenta()
                case "4":
                    agregar_vehiculo()
                case "5":
                    agregar_peaje()
                case "6":
                    agregar_bonificacion()
                case "7":
                    modificar_persona()
                case "8":
                    modificar_propietario()
                case "9":
                    modificar_cuenta()
                case "10":
                    modificar_vehiculo()
                case "11":
                    modificar_peaje()
                case "12":
                    modificar_bonificacion()
                case "13":
                    nuevo_debito()
                case "14":
                    nueva_carga()
                case "15":
                    agregar_tipo_vehiculo()
                case "16":
                    agregar_tarifa()
                case "17":
                    modificar_tipo_de_vehiculo()
                case "18":
                    modificar_tarifa()
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

    displayMenu("menu_de_inicio")


if __name__ == "__main__":
    displayMenu("menu_de_inicio")


