from peewee import AutoField, ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.persona import Persona
from src.models.empresa import Empresa


class Propietario(BaseModel):
    propietario_id = AutoField(primary_key=True)
    propietario_persona = ForeignKeyField(Persona, on_delete='CASCADE', null=True)
    propietario_empresa = ForeignKeyField(Empresa, on_delete='CASCADE', null=True)
