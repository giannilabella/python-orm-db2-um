CREATE TABLE Ventanilla (
    ventanilla_id           SERIAL,
    ventanilla_id_peaje     SERIAL,
    ventanilla_es_rfid      BOOLEAN NOT NULL,
    CONSTRAINT fk
        FOREIGN KEY (ventanilla_id_peaje)
        REFERENCES Peaje(peaje_id)
        ON DELETE CASCADE,
    CONSTRAINT pk
        PRIMARY KEY (ventanilla_id_peaje, ventanilla_id)
);
