CREATE TABLE Debito (
    debito_id               SERIAL      PRIMARY KEY,
    debito_vehiculo_id      SERIAL      NOT NULL,
    debito_peaje_id         SERIAL      NOT NULL,
    debito_ventanilla_id    SERIAL      NOT NULL, 
    debito_fecha_y_hora     TIMESTAMP   NOT NULL,
    debito_cuenta_id        SERIAL      NOT NULL,
    CONSTRAINT fk_vehiculo
        FOREIGN KEY (debito_vehiculo_id)
        REFERENCES Vehiculo(vehiculo_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_ventanilla
        FOREIGN KEY (debito_ventanilla_id, debito_peaje_id)
        REFERENCES Ventanilla(ventanilla_id, ventanilla_peaje_id)
        ON DELETE SET NULL,
    CONSTRAINT fk_cuenta
        FOREIGN KEY (debito_cuenta_id)
        REFERENCES Cuenta(cuenta_id)
        ON DELETE CASCADE
);
