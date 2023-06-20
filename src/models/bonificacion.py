from peewee import AutoField, CharField, SmallIntegerField, DateField, ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.peaje import Peaje
from src.models.cuenta import Cuenta


class Bonificacion(BaseModel):
    bonificacion_id = AutoField(primary_key=True)
    bonificacion_motivo = CharField(max_length=100, null=False)
    bonificacion_descuento = SmallIntegerField(null=False)
    bonificacion_fecha_otorgo = DateField(null=False)
    bonificacion_fecha_renovacion = DateField(null=False)
    bonificacion_id_peaje = ForeignKeyField(Peaje, backref='bonificaciones', on_delete='CASCADE', null=False)
    bonificacion_id_cuenta = ForeignKeyField(Cuenta, backref='bonificaciones', on_delete='CASCADE', null=False)
