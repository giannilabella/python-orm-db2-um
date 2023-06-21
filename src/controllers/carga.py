from src.database import postgres_connect
from src.models.carga import Carga
from src.models.cuenta import Cuenta
from datetime import datetime


def agregar_carga() -> Carga:
    try:
        database = postgres_connect()
    except Exception as e:
        print('Error al conectarse con base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    cuenta_id: str = input("Ingrese cuenta vinculada: ")
    cuenta:Cuenta = None

    try:
        cuenta = Cuenta.get(Cuenta.cuenta_id==cuenta_id)
    except Exception as e:
        database.close()
        print('Error buscando cuenta')
        print(e)
        input('Presione enter para continuar...')
        return

    importe: str = input("Ingrese importe: ")
    
    try:
        new_carga:Carga = Carga.create(
            carga_importe = int(importe),
            carga_fecha_y_hora = datetime.now(),
            carga_cuenta = cuenta,
        )
        cuenta.cuenta_saldo += int(importe)
        cuenta.save()
        database.close()
        print('carga creada')
        input('Presione enter para continuar...')
        return new_carga
    except Exception as e:
        database.close()
        print('Error creando carga')
        print(e)
        input('Presione enter para continuar...')
        return