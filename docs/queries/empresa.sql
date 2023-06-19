CREATE TABLE Empresa (
    empresa_id              SERIAL          PRIMARY KEY,
    empresa_rut             CHAR(12)        NOT NULL,
    empresa_nombre          VARCHAR(35)     NOT NULL, 
    empresa_direccion       VARCHAR(35)     NOT NULL,
    CONSTRAINT unique_attr
        UNIQUE (empresa_rut)
);
