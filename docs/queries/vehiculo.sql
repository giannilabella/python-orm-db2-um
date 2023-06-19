CREATE TABLE Vehiculo(
    vehiculo_id         SERIAL          PRIMARY KEY,
    vehiculo_matricula  CHAR(7)         NOT NULL,
    vehiculo_marca      VARCHAR(35)     NOT NULL, 
    vehiculo_modelo     VARCHAR(35)     NOT NULL,    
    vehiculo_color      VARCHAR(35)     NOT NULL, 
    vehiculo_id_rfid    INTEGER         NOT NULL,
    vehiculo_id_tipo    SERIAL          NOT NULL,
    CONSTRAINT fk
        FOREIGN KEY (vehiculo_id_tipo)
        REFERENCES TipoVehiculo(tipo_vehiculo_id)
        ON DELETE SET NULL,
    CONSTRAINT unique_matricula
        UNIQUE (vehiculo_matricula),
    CONSTRAINT unique_rfid
        UNIQUE (vehiculo_id_rfid)
);
