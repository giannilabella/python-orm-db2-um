from peewee import AutoField, FixedCharField, CharField, IntegerField, ForeignKeyField
from src.models.basemodel import BaseModel


class Peaje(BaseModel):
    peaje_id = AutoField(primary_key=True)
    peaje_ruta = CharField(max_length=35, null=False)
    peaje_nombre = CharField(max_length=35, unique=True, null=False)
    peaje_telefono = FixedCharField(max_length=13, null=False)
    peaje_kilometro = IntegerField(null=False)
    peaje_cantidad_ventanillas = IntegerField(null=False)
