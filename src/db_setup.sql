CREATE TABLE Persona (
    persona_dni,            INT             NOT NULL,
    persona_nombre_1        VARCHAR(35)     NOT NULL,
    persona_nombre_2        VARCHAR(35)     NOT NULL,
    persona_direccion       VARCHAR(35)     NOT NULL,
    persona_apellido_1      VARCHAR(35)     NOT NULL,
    persona_apellido_2      VARCHAR(35)     NOT NULL,
    persona_mail,           VARCHAR(100)    NOT NULL,
    persona_celular,        VARCHAR(13)     NOT NULL,
    persona_dni_asociado    INT             NOT NULL,
    PRIMARY KEY (persona_dni)--,
--    FOREIGN KEY (persona_dni_asociado) REFERENCES Persona(persona_dni)
);

CREATE TABLE Empresa (
    empresa_rut             VARCHAR(12)     NOT NULL,
    empresa_nombre          VARCHAR(35)     NOT NULL, 
    empresa_direccion       VARCHAR(35)     NOT NULL, 
    PRIMARY KEY (empresa_rut)
);

CREATE TABLE Telefono (
    telefono_numero         VARCHAR(13)     NOT NULL,
    telefono_empresa_rut    VARCHAR(12)     NOT NULL,
    PRIMARY KEY (telefono_numero)--,
--    FOREIGN KEY (telefono_empresa_rut) REFERENCES Empresa(empresa_rut)
);

CREATE TABLE Propietario (
    propietario_id                  INT             NOT NULL,
    propietario_persona_dni         VARCHAR(8)      NOT NULL, 
    propietario_empresa_rut         VARCHAR(12)     NOT NULL,    
    PRIMARY KEY (propietario_id),
--    FOREIGN KEY (propietario_empresa_rut) REFERENCES Empresa(empresa_rut),
--    FOREIGN KEY (propietario_persona_dni) REFERENCES Persona(persona_dni)
);

/*
son proyecciones de Propietario de 

CREATE TABLE Propietario_Persona(
    propietario_persona_dni VARCHAR(8) NOT NULL,
    propietario_id          INT        NOT NULL,
    PRIMARY KEY (propietario_persona_dni)
);

CREATE TABLE Propietario_Empresa(
    propietario_empresa_rut VARCHAR(12) NOT NULL,
    propietario_id          INT        NOT NULL,
    PRIMARY KEY (propietario_empresa_rut)
);
*/


CREATE TABLE Cuenta (
    cuenta_numero           INT     NOT NULL, 
    cuenta_creacion         DATE    NOT NULL, 
    cuenta_saldo            INT     NOT NULL,    
    cuenta_propietario_id   INT     NOT NULL,
    PRIMARY KEY (cuenta_numero),
--    FOREIGN KEY (cuenta_propietario_id) REFERENCES Propietario(propietario_id)
);

/*
es proyeccion de cuenta
CREATE TABLE Cuenta_Propietario(
    cuenta_propietario_id   INT     NOT NULL,
    cuenta_numero           INT     NOT NULL,
    PRIMARY KEY (cuenta_propietario_id)
);
*/

CREATE TABLE Carga(
    carga_cuenta_numero INT         NOT NULL,
    carga_fecha_y_hora  DATETIME    NOT NULL,
    carga_importe       INT         NOT NULL,
    PRIMARY KEY (carga_cuenta_numero,carga_fecha_y_hora)
);

CREATE TABLE Vehiculo(
    vehiculo_matricula  INT         NOT NULL,
    vehiculo_marca      VARCHAR(35) NOT NULL, 
    vehiculo_modelo     VARCHAR(35) NOT NULL,    
    vehiculo_color      VARCHAR(35) NOT NULL, 
    vehiculo_id_rfid    INT         NOT NULL, 
    vehiculo_tipo       INT         NOT NULL,
    PRIMARY KEY (vehiculo_matricula),
--    FOREIGN KEY (cuenta_propietario_id) REFERENCES Propietario(propietario_id)
);

/*
es proyeccion
CREATE TABLE Vehiculo_Id_rfid(
    vehiculo_id_rfid    INT         NOT NULL,
    vehiculo_matricula  INT         NOT NULL,
    PRIMARY KEY (vehiculo_id_rfid)
)
*/




--fuente:
--    https://webarchive.nationalarchives.gov.uk/ukgwa/+/http://www.cabinetoffice.gov.uk/media/254290/GDS%20Catalogue%20Vol%202.pdf                                    
