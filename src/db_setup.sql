CREATE TABLE Persona (
    persona_id              INTEGER         SERIAL      PRIMARY KEY,
    persona_dni             CHAR(8)         NOT NULL    UNIQUE,
    persona_nombre_1        VARCHAR(35)     NOT NULL,
    persona_nombre_2        VARCHAR(35)     NOT NULL,
    persona_direccion       VARCHAR(35)     NOT NULL,
    persona_apellido_1      VARCHAR(35)     NOT NULL,
    persona_apellido_2      VARCHAR(35)     NOT NULL,
    persona_mail,           VARCHAR(100)    NOT NULL,
    persona_celular,        VARCHAR(13)     NOT NULL,
    persona_dni_asociado    INTEGER         NOT NULL    references Empresa(persona_id)
);

CREATE TABLE Empresa (
    empresa_id              INTEGER         SERIAL      PRIMARY KEY,
    empresa_rut             CHAR(12)        NOT NULL    UNIQUE,
    empresa_nombre          VARCHAR(35)     NOT NULL, 
    empresa_direccion       VARCHAR(35)     NOT NULL
);

CREATE TABLE Telefono (
    telefono_id             INTEGER         SERIAL      PRIMARY KEY,
    telefono_numero         CHAR(13)        NOT NULL    UNIQUE,
    telefono_empresa_rut    CHAR(12)        NOT NULL
);

CREATE TABLE Propietario (
    propietario_id                 INTEGER     SERIAL       PRIMARY KEY,
    propietario_persona_id         INTEGER     NOT NULL     references Persona(persona_id), 
    propietario_empresa_id         INTEGER     NOT NULL     references Empresa(empresa_id)
);

CREATE TABLE Cuenta (
    cuenta_numero           INTEGER     SERIAL      PRIMARY KEY, 
    cuenta_creacion         DATE        NOT NULL, 
    cuenta_saldo            INTEGER     NOT NULL,    
    cuenta_propietario_id   INTEGER     NOT NULL    references Propietario(propietario_id)
);

CREATE TABLE Carga(
    carga_id            INTEGER         SERIAL      PRIMARY KEY,
    carga_cuenta_numero INTEGER         NOT NULL    references Cuenta(cuenta_numero),
    carga_fecha_y_hora  TIMESTAMP       NOT NULL,
    carga_importe       INTEGER         NOT NULL
);

CREATE TABLE Vehiculo(
    vehiculo_id         INTEGER         SERIAL      PRIMARY KEY,
    vehiculo_matricula  CHAR(7)         NOT NULL    UNIQUE,
    vehiculo_marca      VARCHAR(35)     NOT NULL, 
    vehiculo_modelo     VARCHAR(35)     NOT NULL,    
    vehiculo_color      VARCHAR(35)     NOT NULL, 
    vehiculo_id_rfid    INTEGER         NOT NULL    UNIQUE, 
    vehiculo_tipo_id    INTEGER         NOT NULL    references TipoVehiculo(tipo_vehiculo_id)
);

CREATE TABLE TipoVehiculo(
    tipo_vehiculo_id    INTEGER         SERIAL      PRIMARY KEY,
    tipo_vehiculo_tipo  VARCHAR(35)     NOT NULL    UNIQUE,
);

CREATE TABLE Tarifa(
    tarifa_id                   INTEGER             SERIAL      PRIMARY KEY,
    tarifa_tipo_vehiculo_id     INTEGER             NOT NULL    references TipoVehiculo(tipo_vehiculo_id),
    tarifa_fecha                DATE                NOT NULL,
    tarifa_valor                INTEGER             NOT NULL
);

CREATE TABLE Peaje(
    peaje_id                    INTEGER             SERIAL      PRIMARY KEY,
    peaje_nombre                VARCHAR(35)         NOT NULL    UNIQUE,
    peaje_ruta                  VARCHAR(35)         NOT NULL, 
    peaje_kilometro             INTEGER             NOT NULL, 
    peaje_telefono              VARCHAR(13)         NOT NULL, 
    peaje_cantidad_ventanillas  INTEGER             NOT NULL
);

CREATE TABLE Ventanilla(
    ventanilla_peaje_id         INTEGER             NOT NULL    references Peaje(peaje_id),
    ventanilla_id               INTEGER             NOT NULL,
    ventanilla_es_rfid          BOOLEAN             NOT NULL,
    PRIMARY KEY (ventanilla_peaje_nombre,ventanilla_id)
);

CREATE TABLE Debito(
    debito_id                   INTEGER         SERIAL      PRIMARY KEY,
    debito_vehiculo_id          INTEGER         NOT NULL    references Vehiculo(vehiculo_id),
    debioto_peaje_id            INTEGER         NOT NULL    references Peaje(peaje_id),
    debito_ventanilla_id        INTEGER         NOT NULL    references Ventanilla(ventanilla_id), 
    debito_fecha_y_hora         TIMESTAMP       NOT NULL,
    debito_cuenta_numero        INTEGER         NOT NULL    references Cuenta(cuenta_numero)
);


CREATE TABLE Bonificacion(
    bonificacion_id                 INTEGER         SERIAL      PRIMARY KEY,
    bonificacion_cuenta_numero      INTEGER         NOT NULL    references Cuenta(cuenta_numero), 
    bonificacion_fecha_otorgo       DATE            NOT NULL, 
    bonificacion_descuento          SMALLINT        NOT NULL, 
    bonificacion_motivo             VARCHAR(100)    NOT NULL,
    bonificacion_peaje_id           INTEGER         NOT NULL    references Peaje(peaje_id), 
    bonificacion_fecha_renovacion   DATE            NOT NULL
);

CREATE TABLE Propietario_Vehiculo(
    propietario_id  INTEGER NOT NULL references Propietario(propietario_id),
    vehiculo_id     INTEGER NOT NULL references Vehiculo(vehiculo_id)
);

--fuentes:
--    https://webarchive.nationalarchives.gov.uk/ukgwa/+/http://www.cabinetoffice.gov.uk/media/254290/GDS%20Catalogue%20Vol%202.pdf                                    
--    https://es.wikipedia.org/wiki/Patente_%C3%9Anica_del_Mercosur