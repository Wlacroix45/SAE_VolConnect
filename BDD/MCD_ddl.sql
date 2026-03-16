DROP TABLE IF EXISTS vol;
CREATE TABLE vol (
  PRIMARY KEY (id_vol),
  id_vol             VARCHAR(42) NOT NULL,
  nom_vol            VARCHAR(42),
  date_heure_depart  VARCHAR(42),
  date_heure_arrivee VARCHAR(42),
  nom_comp           VARCHAR(42),
  nom_terminal       VARCHAR(42),
  ville              VARCHAR(42),
  pays               VARCHAR(42)
);