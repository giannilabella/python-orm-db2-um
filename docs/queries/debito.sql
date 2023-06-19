CREATE TABLE Debito (
    debito_id               SERIAL      PRIMARY KEY,
    debito_id_vehiculo      SERIAL      NOT NULL,
    debito_id_peaje         SERIAL      NOT NULL,
    debito_id_ventanilla    SERIAL      NOT NULL, 
    debito_fecha_y_hora     TIMESTAMP   NOT NULL,
    debito_id_cuenta        SERIAL      NOT NULL,
    CONSTRAINT fk_vehiculo
        FOREIGN KEY (debito_id_vehiculo)
        REFERENCES Vehiculo(vehiculo_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_ventanilla
        FOREIGN KEY (debito_id_ventanilla, debito_id_peaje)
        REFERENCES Ventanilla(ventanilla_id, ventanilla_id_peaje)
        ON DELETE SET NULL,
    CONSTRAINT fk_cuenta
        FOREIGN KEY (debito_id_cuenta)
        REFERENCES Cuenta(cuenta_id)
        ON DELETE CASCADE
);
