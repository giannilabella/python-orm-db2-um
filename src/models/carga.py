from peewee import AutoField, IntegerField, DateTimeField, ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.cuenta import Cuenta


class Carga(BaseModel):
    carga_id = AutoField(primary_key=True)
    carga_importe = IntegerField(null=False)
    carga_fecha_y_hora = DateTimeField(null=False)
    carga_cuenta = ForeignKeyField(Cuenta, backref='cargas', on_delete='CASCADE')
