CREATE TABLE Carga(
    carga_id            SERIAL      PRIMARY KEY,
    carga_fecha_y_hora  TIMESTAMP   NOT NULL,
    carga_importe       INTEGER     NOT NULL,
    carga_cuenta_id     SERIAL      NOT NULL,
    CONSTRAINT fk
        FOREIGN KEY (carga_cuenta_id)
        REFERENCES Cuenta(cuenta_id)
        ON DELETE SET NULL
);
