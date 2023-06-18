CREATE TABLE Persona (
    persona_id              INT             SERIAL      PRIMARY KEY,
    persona_dni             CHAR(8)         NOT NULL,
    persona_nombre_1        VARCHAR(35)     NOT NULL,
    persona_nombre_2        VARCHAR(35)     NOT NULL,
    persona_direccion       VARCHAR(35)     NOT NULL,
    persona_apellido_1      VARCHAR(35)     NOT NULL,
    persona_apellido_2      VARCHAR(35)     NOT NULL,
    persona_mail,           VARCHAR(100)    NOT NULL,
    persona_celular,        VARCHAR(13)     NOT NULL,
    persona_dni_asociado    INT             NOT NULL
);

CREATE TABLE Empresa (
    empresa_id              INT             SERIAL      PRIMARY KEY,
    empresa_rut             CHAR(12)        NOT NULL,
    empresa_nombre          VARCHAR(35)     NOT NULL, 
    empresa_direccion       VARCHAR(35)     NOT NULL
);

CREATE TABLE Telefono (
    telefono_id             INT             SERIAL      PRIMARY KEY,
    telefono_numero         CHAR(13)        NOT NULL,
    telefono_empresa_rut    CHAR(12)        NOT NULL
);

CREATE TABLE Propietario (
    propietario_id                 INT     SERIAL       PRIMARY KEY,
    propietario_persona_id         INT     NOT NULL, 
    propietario_empresa_id         INT     NOT NULL
);

CREATE TABLE Cuenta (
    cuenta_numero           INT     SERIAL      PRIMARY KEY, 
    cuenta_creacion         DATE    NOT NULL, 
    cuenta_saldo            INT     NOT NULL,    
    cuenta_propietario_id   INT     NOT NULL
);

CREATE TABLE Carga(
    carga_id            INT         SERIAL      PRIMARY KEY,
    carga_cuenta_numero INT         NOT NULL,
    carga_fecha_y_hora  DATETIME    NOT NULL,
    carga_importe       INT         NOT NULL
);

CREATE TABLE Vehiculo(
    vehiculo_id         INT             SERIAL      PRIMARY KEY,
    vehiculo_matricula  CHAR(7)         NOT NULL,
    vehiculo_marca      VARCHAR(35)     NOT NULL, 
    vehiculo_modelo     VARCHAR(35)     NOT NULL,    
    vehiculo_color      VARCHAR(35)     NOT NULL, 
    vehiculo_id_rfid    INT             NOT NULL, 
    vehiculo_tipo       VARCHAR(35)     NOT NULL
);

CREATE TABLE Tarifa(
    tarifa_id                   INT             SERIAL      PRIMARY KEY,
    tarifa_tipo_vehiculo_tipo   VARCHAR(35)     NOT NULL,
    tarifa_fecha                DATE            NOT NULL,
    tarifa_valor                INT             NOT NULL
);

CREATE TABLE Peaje(
    peaje_id                    INT             SERIAL      PRIMARY KEY,
    peaje_nombre                VARCHAR(35)     NOT NULL,
    peaje_ruta                  VARCHAR(35)     NOT NULL, 
    peaje_kilometro             INT             NOT NULL, 
    peaje_telefono              VARCHAR(13)     NOT NULL, 
    peaje_cantidad_ventanillas  INT             NOT NULL
);

CREATE TABLE Ventanilla(
    ventanilla_peaje_id         INT             NOT NULL,
    ventanilla_numero           INT             NOT NULL,
    ventanilla_es_rfid          BOOLEAN         NOT NULL,
    PRIMARY KEY (ventanilla_peaje_nombre,ventanilla_numero)
);

CREATE TABLE Debito(
    debito_id                   INT         SERIAL      PRIMARY KEY,
    debito_vehiculo_matricula   VARCHAR(7)  NOT NULL,
    debito_ventanilla_numero    INT         NOT NULL, 
    debito_fecha_y_hora         DATETIME    NOT NULL,
    debito_cuenta_numero        INT         NOT NULL,
);


--fuentes:
--    https://webarchive.nationalarchives.gov.uk/ukgwa/+/http://www.cabinetoffice.gov.uk/media/254290/GDS%20Catalogue%20Vol%202.pdf                                    
--    https://es.wikipedia.org/wiki/Patente_%C3%9Anica_del_Mercosur