CREATE TABLE Telefono (
    telefono_id             SERIAL      PRIMARY KEY,
    telefono_numero         CHAR(13)    NOT NULL,
    telefono_empresa_id     SERIAL      NOT NULL,
    CONSTRAINT fk_empresa
        FOREIGN KEY (telefono_empresa_id)
        REFERENCES Empresa(empresa_id)
        ON DELETE CASCADE
);
