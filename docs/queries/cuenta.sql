CREATE TABLE Cuenta (
	cuenta_id               SERIAL  PRIMARY KEY,
    cuenta_saldo            INTEGER NOT NULL,
    cuenta_creacion         DATE    NOT NULL,
    cuenta_propietario_id   SERIAL  NOT NULL,
    CONSTRAINT fk_propietario
        FOREIGN KEY (cuenta_propietario_id)
        REFERENCES Propietario(propietario_id)
        ON DELETE CASCADE
);
