from src.models.persona import Persona
from src.models.empresa import Empresa
from src.models.telefono import Telefono
from src.models.propietario import Propietario
from src.models.cuenta import Cuenta
from src.models.carga import Carga
from src.models.vehiculo import Vehiculo
from src.models.tipo_vehiculo import TipoVehiculo
from src.models.tarifa import Tarifa
from src.models.peaje import Peaje
from src.models.ventanilla import Ventanilla
from src.models.bonificacion import Bonificacion
from src.models.debito import Debito
from src.models.propietario_vehiculo import PropietarioVehiculo

from src.database import postgres_connect


def create_tables():
    print('Connecting to database...')
    database = postgres_connect()
    print('Connected to database!')

    print('Creating tables...')
    database.create_tables([
        Persona,
        Empresa,
        Propietario,
        Telefono,
        Propietario,
        Cuenta,
        Carga,
        Vehiculo,
        TipoVehiculo,
        Tarifa,
        Peaje,
        Ventanilla,
        Bonificacion,
        Debito,
        PropietarioVehiculo,
    ])
    print('Tables created!')


def drop_tables():
    print('Connecting to database...')
    database = postgres_connect()
    print('Connected to database!')

    print('Dropping tables...')
    database.drop_tables([
        Persona,
        Empresa,
        Propietario,
        Telefono,
        Propietario,
        Cuenta,
        Carga,
        Vehiculo,
        TipoVehiculo,
        Tarifa,
        Peaje,
        Ventanilla,
        Bonificacion,
        Debito,
        PropietarioVehiculo,
    ])
    print('Tables dropped!')
