CREATE TABLE Propietario_Vehiculo(
    propietario_vehiculo_propietario_id  SERIAL  NOT NULL,
    propietario_vehiculo_vehiculo_id     SERIAL  NOT NULL,
    CONSTRAINT fk_propietario
        FOREIGN KEY (propietario_vehiculo_propietario_id)
        REFERENCES Propietario(propietario_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_vehiculo
        FOREIGN KEY (propietario_vehiculo_vehiculo_id)
        REFERENCES Vehiculo(vehiculo_id)
        ON DELETE CASCADE,
    CONSTRAINT pk_prop_vehi
        PRIMARY KEY (propietario_vehiculo_propietario_id, id_vehiculo)
);
