from peewee import AutoField, FixedCharField, ForeignKeyField
from src.models.basemodel import BaseModel


class Telefono(BaseModel):
    telefono_id = AutoField(primary_key=True)
    telefono_numero = FixedCharField(max_length=13, unique=True)
    telefono_id_empresa = ForeignKeyField('self', on_delete='CASCADE', null=True)
