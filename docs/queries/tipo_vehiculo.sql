CREATE TABLE TipoVehiculo(
    tipo_vehiculo_id    SERIAL      PRIMARY KEY,
    tipo_vehiculo_tipo  VARCHAR(35) NOT NULL,
    CONSTRAINT unique_tipo
        UNIQUE (tipo_vehiculo_tipo)
);
