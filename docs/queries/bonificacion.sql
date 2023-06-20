CREATE TABLE Bonificacion(
    bonificacion_id                 SERIAL          PRIMARY KEY,
    bonificacion_fecha_otorgo       DATE            NOT NULL, 
    bonificacion_descuento          SMALLINT        NOT NULL, 
    bonificacion_motivo             VARCHAR(100)    NOT NULL,
    bonificacion_fecha_renovacion   DATE            NOT NULL,
    bonificacion_peaje_id           SERIAL          NOT NULL, 
    bonificacion_cuenta_id          SERIAL          NOT NULL, 
    CONSTRAINT fk_peaje
        FOREIGN KEY (bonificacion_peaje_id)
        REFERENCES Peaje(peaje_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_cuenta
        FOREIGN KEY (bonificacion_cuenta_id)
        REFERENCES Cuenta(cuenta_id)
        ON DELETE CASCADE
);
