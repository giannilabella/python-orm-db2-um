CREATE TABLE Propietario (
	propietario_id          SERIAL  PRIMARY KEY,
    propietario_id_persona  SERIAL,
    propietario_id_empresa  SERIAL,
    CONSTRAINT fk_persona
        FOREIGN KEY (propietario_id_persona)
        REFERENCES Persona(persona_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_empresa
        FOREIGN KEY (propietario_id_empresa)
        REFERENCES Empresa(empresa_id)
        ON DELETE CASCADE
);
