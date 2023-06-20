from peewee import AutoField, FixedCharField, CharField, IntegerField, ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.tipo_vehiculo import TipoVehiculo


class Vehiculo(BaseModel):
    vehiculo_id = AutoField(primary_key=True)
    vehiculo_marca = CharField(max_length=35, null=False)
    vehiculo_color = CharField(max_length=35, null=False)
    vehiculo_modelo = CharField(max_length=35, null=False)
    vehiculo_id_rfid = IntegerField(unique=True, null=False)
    vehiculo_matricula = FixedCharField(max_length=7, unique=True, null=False)
    vehiculo_tipo = ForeignKeyField(TipoVehiculo, on_delete='SET NULL', null=False)
