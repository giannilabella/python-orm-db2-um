from peewee import AutoField, FixedCharField, CharField
from src.models.basemodel import BaseModel


class Empresa(BaseModel):
    empresa_id = AutoField(primary_key=True)
    empresa_rut = FixedCharField(max_length=12, unique=True, null=False)
    empresa_nombre = CharField(max_length=35, null=False)
    empresa_direccion = CharField(max_length=100, null=False)
