CREATE TABLE Propietario (
	propietario_id          SERIAL  PRIMARY KEY,
    propietario_persona_id  SERIAL,
    propietario_empresa_id  SERIAL,
    CONSTRAINT fk_persona
        FOREIGN KEY (propietario_persona_id)
        REFERENCES Persona(persona_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_empresa
        FOREIGN KEY (propietario_empresa_id)
        REFERENCES Empresa(empresa_id)
        ON DELETE CASCADE
);
