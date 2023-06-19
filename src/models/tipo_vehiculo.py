from peewee import AutoField, CharField
from src.models.basemodel import BaseModel


class TipoVehiculo(BaseModel):
    tipo_vehiculo_id = AutoField(primary_key=True)
    tipo_vehiculo_tipo = CharField(max_length=35, unique=True, null=False)
