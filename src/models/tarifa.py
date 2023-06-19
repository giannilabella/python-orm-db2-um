from peewee import AutoField, IntegerField, DateField, ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.tipovehiculo import TipoVehiculo


class Tarifa(BaseModel):
    tarifa_id = AutoField(primary_key=True)
    tarifa_valor = IntegerField(null=False)
    tarifa_fecha = DateField(null=False)
    tarifa_id_tipo_vehiculo = ForeignKeyField(TipoVehiculo, null=False)
