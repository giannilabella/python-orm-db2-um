from peewee import *

from database import *

class Persona(Model):
    persona_id = PrimaryKeyField()
    persona_dni = CharField(max_length=8, unique=True)
    persona_nombre_1 = CharField(max_length=35)
    persona_nombre_2 = CharField(max_length=35)
    persona_direccion = CharField(max_length=35)
    persona_apellido_1 = CharField(max_length=35)
    persona_apellido_2 = CharField(max_length=35)
    persona_mail = CharField(max_length=100)
    persona_celular = CharField(max_length=13)
    persona_dni_asociado = IntegerField()

    class Meta:
        database = postgres_db

class Empresa(Model):
    empresa_id = PrimaryKeyField()
    empresa_rut = CharField(max_length=12, unique=True)
    empresa_nombre = CharField(max_length=35)
    empresa_direccion = CharField(max_length=35)

    class Meta:
        database = postgres_db

class Telefono(Model):
    telefono_id = PrimaryKeyField()
    telefono_numero = CharField(max_length=13, unique=True)
    telefono_empresa_rut = CharField(max_length=12)

    class Meta:
        database = postgres_db

class Propietario(Model):
    propietario_id = PrimaryKeyField()
    propietario_persona_id = ForeignKeyField(Persona, backref='propietarios')
    propietario_empresa_id = ForeignKeyField(Empresa, backref='propietarios')

    class Meta:
        database = postgres_db

class Cuenta(Model):
    cuenta_numero = PrimaryKeyField()
    cuenta_creacion = DateField()
    cuenta_saldo = IntegerField()
    cuenta_propietario_id = ForeignKeyField(Propietario, backref='cuentas')

    class Meta:
        database = postgres_db

class Carga(Model):
    carga_id = PrimaryKeyField()
    carga_cuenta_numero = ForeignKeyField(Cuenta, backref='cargas')
    carga_fecha_y_hora = DateTimeField()
    carga_importe = IntegerField()

    class Meta:
        database = postgres_db

class TipoVehiculo(Model):
    tipo_vehiculo_id = PrimaryKeyField()
    tipo_vehiculo_tipo = CharField(max_length=35, unique=True)

    class Meta:
        database = postgres_db

class Vehiculo(Model):
    vehiculo_id = PrimaryKeyField()
    vehiculo_matricula = CharField(max_length=7, unique=True)
    vehiculo_marca = CharField(max_length=35)
    vehiculo_modelo = CharField(max_length=35)
    vehiculo_color = CharField(max_length=35)
    vehiculo_id_rfid = IntegerField(unique=True)
    vehiculo_tipo_id = ForeignKeyField(TipoVehiculo, backref='vehiculos')

    class Meta:
        database = postgres_db

class Tarifa(Model):
    tarifa_id = PrimaryKeyField()
    tarifa_tipo_vehiculo_id = ForeignKeyField(TipoVehiculo, backref='tarifas')
    tarifa_fecha = DateField()
    tarifa_valor = IntegerField()

    class Meta:
        database=postgres_db

class Peaje(Model):
    peaje_id=PrimaryKeyField()
    peaje_nombre=CharField(max_length=35,unique=True)
    peaje_ruta=CharField(max_length=35)
    peaje_kilometro=IntegerField()
    peaje_telefono=CharField(max_length=13)
    peaje_cantidad_ventanillas=IntegerField()

class Ventanilla(Model):
  ventanilla_peaje_id=ForeignKeyField(Peaje,backref='ventanillas')
  ventanilla_numero=IntegerField()
  ventanilla_es_rfid=BooleanField()

  class Meta:
      primary_key=CompositeKey('ventanilla_peaje_id','ventanilla_numero')

class Bonificacion(Model):
    bonificacion_id = PrimaryKeyField()
    bonificacion_cuenta_numero = ForeignKeyField(Cuenta, backref='bonificaciones')
    bonificacion_fecha_otorgo = DateField()
    bonificacion_descuento = SmallIntegerField()
    bonificacion_motivo = CharField(max_length=100)
    bonificacion_peaje_id = ForeignKeyField(Peaje, backref='bonificaciones')
    bonificacion_fecha_renovacion = DateField()

    class Meta:
        database = postgres_db

class Debito(Model):
    debito_id = PrimaryKeyField()
    debito_vehiculo_id = ForeignKeyField(Vehiculo, backref='debitos')
    debito_peaje_id = ForeignKeyField(Peaje, backref='debitos')
    debito_ventanilla_numero = ForeignKeyField(Ventanilla, backref='debitos')
    debito_fecha_y_hora = DateTimeField()
    debito_cuenta_numero = ForeignKeyField(Cuenta, backref='debitos')

    class Meta:
        database = postgres_db
