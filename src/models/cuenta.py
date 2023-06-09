from peewee import AutoField, IntegerField, DateField, ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.propietario import Propietario


class Cuenta(BaseModel):
    cuenta_id = AutoField(primary_key=True)
    cuenta_saldo = IntegerField(null=False)
    cuenta_creacion = DateField(null=False)
    cuenta_propietario = ForeignKeyField(Propietario, on_delete='CASCADE', unique=True)
