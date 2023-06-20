from peewee import AutoField, BooleanField, ForeignKeyField
from src.models.basemodel import BaseModel
from src.models.peaje import Peaje


class Ventanilla(BaseModel):
    ventanilla_id = AutoField(primary_key=True)
    ventanilla_es_rfid = BooleanField(null=False)
    ventanilla_id_peaje = ForeignKeyField(Peaje, backref='ventanillas', on_delete='CASCADE')
