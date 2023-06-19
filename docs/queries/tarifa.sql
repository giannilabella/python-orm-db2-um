CREATE TABLE Tarifa(
    tarifa_id                   SERIAL      PRIMARY KEY,
    tarifa_fecha                DATE        NOT NULL,
    tarifa_valor                INTEGER     NOT NULL,
    tarifa_id_tipo_vehiculo     INTEGER     NOT NULL,
    CONSTRAINT fk
        FOREIGN KEY (tarifa_id_tipo_vehiculo)
        REFERENCES TipoVehiculo(tipo_vehiculo_id)
        ON DELETE CASCADE
);
