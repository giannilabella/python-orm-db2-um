CREATE TABLE Carga(
    carga_id            SERIAL      PRIMARY KEY,
    carga_fecha_y_hora  TIMESTAMP   NOT NULL,
    carga_importe       INTEGER     NOT NULL,
    carga_id_cuenta     SERIAL      NOT NULL,
    CONSTRAINT fk
        FOREIGN KEY (carga_id_cuenta)
        REFERENCES Cuenta(cuenta_id)
        ON DELETE SET NULL
);
