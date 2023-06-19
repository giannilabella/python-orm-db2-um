from peewee import AutoField, FixedCharField, CharField, ForeignKeyField
from src.models.basemodel import BaseModel


class Persona(BaseModel):
    persona_id = AutoField(primary_key=True)
    persona_dni = FixedCharField(max_length=8, unique=True, null=False)
    persona_mail = CharField(max_length=50, null=False)
    persona_celular = FixedCharField(max_length=13, null=False)
    persona_nombre_1 = CharField(max_length=35, null=False)
    persona_nombre_2 = CharField(max_length=35, null=True)
    persona_direccion = CharField(max_length=100, null=False)
    persona_apellido_1 = CharField(max_length=35, null=False)
    persona_apellido_2 = CharField(max_length=35, null=True)
    persona_id_asociado = ForeignKeyField('self', on_delete='SET NULL', null=True)
