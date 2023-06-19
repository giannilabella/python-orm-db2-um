CREATE TABLE Bonificacion(
    bonificacion_id                 SERIAL          PRIMARY KEY,
    bonificacion_fecha_otorgo       DATE            NOT NULL, 
    bonificacion_descuento          SMALLINT        NOT NULL, 
    bonificacion_motivo             VARCHAR(100)    NOT NULL,
    bonificacion_fecha_renovacion   DATE            NOT NULL,
    bonificacion_id_peaje           SERIAL          NOT NULL, 
    bonificacion_id_cuenta          SERIAL          NOT NULL, 
    CONSTRAINT fk_peaje
        FOREIGN KEY (bonificacion_id_peaje)
        REFERENCES Peaje(peaje_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_cuenta
        FOREIGN KEY (bonificacion_id_cuenta)
        REFERENCES Cuenta(cuenta_id)
        ON DELETE CASCADE
);
