CREATE TABLE Cuenta (
	cuenta_id               SERIAL  PRIMARY KEY,
    cuenta_saldo            INTEGER NOT NULL,
    cuenta_creacion         DATE    NOT NULL,
    cuenta_id_propietario   SERIAL  NOT NULL,
    CONSTRAINT fk_propietario
        FOREIGN KEY (cuenta_id_propietario)
        REFERENCES Propietario(propietario_id)
        ON DELETE CASCADE
);
