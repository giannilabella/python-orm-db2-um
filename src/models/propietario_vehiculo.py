from peewee import ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.propietario import Propietario
from src.models.vehiculo import Vehiculo


class PropietarioVehiculo(BaseModel):
    id_propietario = ForeignKeyField(Propietario, backref='vehiculos', primary_key=True)
    id_vehiculo = ForeignKeyField(Vehiculo, backref='propietarios', primary_key=True)
