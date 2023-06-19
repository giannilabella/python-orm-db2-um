from src.database import postgres_database
from peewee import Model


class BaseModel(Model):
    class Meta:
        database = postgres_database
