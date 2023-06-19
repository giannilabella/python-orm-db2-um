CREATE TABLE Persona (
    persona_id              SERIAL          PRIMARY KEY,
    persona_dni             CHAR(8)         NOT NULL,
    persona_mail            VARCHAR(100)    NOT NULL,
    persona_celular         VARCHAR(13)     NOT NULL,
    persona_nombre_1        VARCHAR(35)     NOT NULL,
    persona_nombre_2        VARCHAR(35)     NOT NULL,
    persona_direccion       VARCHAR(35)     NOT NULL,
    persona_apellido_1      VARCHAR(35)     NOT NULL,
    persona_apellido_2      VARCHAR(35)     NOT NULL,
    persona_id_asociado     SERIAL,
    CONSTRAINT fk_asociado
        FOREIGN KEY (persona_id_asociado)
        REFERENCES Persona(persona_id)
        ON DELETE SET NULL,
    CONSTRAINT unique_attr
        UNIQUE (persona_dni)
);
