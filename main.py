from src.controllers.empresa import *
from src.controllers.peaje import *
from src.controllers.ventanilla import *
import src.utils
if __name__ == "__main__":
#    src.utils.drop_tables()
#    src.utils.create_tables()
    agregar_peaje()
    agregar_ventanilla()
    modificar_ventanilla()
    borrar_ventanilla()

    