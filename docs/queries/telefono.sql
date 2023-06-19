CREATE TABLE Telefono (
    telefono_id             SERIAL      PRIMARY KEY,
    telefono_numero         CHAR(13)    NOT NULL,
    telefono_id_empresa     SERIAL      NOT NULL,
    CONSTRAINT fk_empresa
        FOREIGN KEY (telefono_id_empresa)
        REFERENCES Empresa(empresa_id)
        ON DELETE CASCADE
);
