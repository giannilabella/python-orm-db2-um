CREATE TABLE Ventanilla (
    ventanilla_id           SERIAL,
    ventanilla_peaje_id     SERIAL,
    ventanilla_es_rfid      BOOLEAN NOT NULL,
    CONSTRAINT fk
        FOREIGN KEY (ventanilla_peaje_id)
        REFERENCES Peaje(peaje_id)
        ON DELETE CASCADE,
    CONSTRAINT pk
        PRIMARY KEY (ventanilla_peaje_id, ventanilla_id)
);
