from peewee import AutoField, DateTimeField, ForeignKeyField,IntegerField
from src.models.basemodel import BaseModel
from src.models.cuenta import Cuenta
from src.models.peaje import Peaje
from src.models.vehiculo import Vehiculo
from src.models.ventanilla import Ventanilla


class Debito(BaseModel):
    debito_id = AutoField(primary_key=True)
    debito_fecha_y_hora = DateTimeField(null=False)
    debito_cuenta = ForeignKeyField(Cuenta, backref='debitos', on_delete='CASCADE')
    debito_peaje = ForeignKeyField(Peaje, backref='debitos', on_delete='SET NULL')
    debito_vehiculo = ForeignKeyField(Vehiculo, backref='debitos', on_delete='SET NULL')
    debito_ventanilla = ForeignKeyField(Ventanilla, backref='debitos', on_delete='SET NULL')
    debito_monto = IntegerField(null=False)