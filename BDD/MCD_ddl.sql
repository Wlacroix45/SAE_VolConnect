


DROP TABLE IF EXISTS partir;
DROP TABLE IF EXISTS arriver;
DROP TABLE IF EXISTS localiser;
DROP TABLE IF EXISTS vol;
DROP TABLE IF EXISTS terminal;
DROP TABLE IF EXISTS companie;
DROP TABLE IF EXISTS aeroport;

CREATE TABLE aeroport (
  PRIMARY KEY (id_aeroport),
  id_aeroport int NOT NULL,
  nom_aeroport         VARCHAR(42),
  ville       VARCHAR(42),
  pays        VARCHAR(42)
);

CREATE TABLE companie (
  PRIMARY KEY (id_companie),
  id_companie int NOT NULL,
  nom_comp    VARCHAR(42)
);

CREATE TABLE localiser (
  PRIMARY KEY (id_companie, id_aeroport),
  id_companie int NOT NULL,
  id_aeroport int NOT NULL
);

CREATE TABLE terminal (
  PRIMARY KEY (id_terminal),
  id_terminal int NOT NULL,
  nom_terminal         VARCHAR(42),
  id_aeroport int NOT NULL
);

CREATE TABLE vol (
  PRIMARY KEY (id_vol),
  id_vol              int NOT NULL,
  nom_vol             VARCHAR(42),
  correspondance      VARCHAR(42),
  id_companie         int NOT NULL
);

CREATE TABLE arriver (
  PRIMARY KEY (id_terminal,id_vol),
  id_terminal int NOT NULL,
  id_vol              int NOT NULL,
  nom_terminal         VARCHAR(42),
  id_aeroport int NOT NULL,
  date_heure_arrivee Date
);

CREATE TABLE partir (
  PRIMARY KEY (id_terminal,id_vol),
  id_terminal int NOT NULL,
  id_vol              int NOT NULL,
  nom_terminal         VARCHAR(42),
  id_aeroport int NOT NULL,
  date_heure_depart Date
);

ALTER TABLE localiser ADD FOREIGN KEY (id_aeroport) REFERENCES aeroport (id_aeroport);
ALTER TABLE localiser ADD FOREIGN KEY (id_companie) REFERENCES companie (id_companie);

ALTER TABLE terminal ADD FOREIGN KEY (id_aeroport) REFERENCES aeroport (id_aeroport);

ALTER TABLE vol ADD FOREIGN KEY (id_companie) REFERENCES companie (id_companie);

ALTER TABLE arriver ADD FOREIGN KEY (id_terminal) REFERENCES terminal (id_terminal);
ALTER TABLE arriver ADD FOREIGN KEY (id_vol) REFERENCES vol (id_vol);

ALTER TABLE partir ADD FOREIGN KEY (id_terminal) REFERENCES terminal (id_terminal);
ALTER TABLE partir ADD FOREIGN KEY (id_vol) REFERENCES vol (id_vol);