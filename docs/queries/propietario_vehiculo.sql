CREATE TABLE Propietario_Vehiculo(
    id_propietario  SERIAL  NOT NULL,
    id_vehiculo     SERIAL  NOT NULL,
    CONSTRAINT fk_propietario
        FOREIGN KEY (id_propietario)
        REFERENCES Propietario(propietario_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_vehiculo
        FOREIGN KEY (id_vehiculo)
        REFERENCES Vehiculo(vehiculo_id)
        ON DELETE CASCADE,
    CONSTRAINT pk_prop_vehi
        PRIMARY KEY (id_propietario, id_vehiculo)
);
