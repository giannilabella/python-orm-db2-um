from peewee import ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.propietario import Propietario
from src.models.vehiculo import Vehiculo


class PropietarioVehiculo(BaseModel):
    propietario_vehiculo_propietario = ForeignKeyField(Propietario, backref='vehiculos', on_delete='CASCADE')
    propietario_vehiculo_vehiculo = ForeignKeyField(Vehiculo, backref='propietarios', on_delete='CASCADE')
