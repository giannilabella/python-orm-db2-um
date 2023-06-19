CREATE TABLE Peaje (
    peaje_id                    SERIAL              PRIMARY KEY,
    peaje_nombre                VARCHAR(35)         NOT NULL,
    peaje_ruta                  VARCHAR(35)         NOT NULL, 
    peaje_kilometro             INTEGER             NOT NULL, 
    peaje_telefono              VARCHAR(13)         NOT NULL, 
    peaje_cantidad_ventanillas  INTEGER             NOT NULL,
    CONSTRAINT unique_peaje_nombre
        UNIQUE (peaje_nombre)
);
