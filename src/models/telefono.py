from peewee import AutoField, FixedCharField, ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.empresa import Empresa

class Telefono(BaseModel):
    telefono_id = AutoField(primary_key=True)
    telefono_numero = FixedCharField(max_length=13, unique=True)
    telefono_id_empresa = ForeignKeyField(Empresa, on_delete='CASCADE', null=False)
