DROP TABLE IF EXISTS vol;
CREATE TABLE vol (
  PRIMARY KEY (id_comp, id_vol, date_heure_depart),
  id_vol             VARCHAR(42) NOT NULL,
  nom_vol            VARCHAR(42),
  date_heure_depart  VARCHAR(42),
  date_heure_arrivee VARCHAR(42),
  id_comp           VARCHAR(42),
  nom_terminal_dep       VARCHAR(42),
  nom_terminal_arr  VARCHAR(42),
  ville_dep              VARCHAR(42),
  ville_arr     VARCHAR(42),
  pays_dep               VARCHAR(42),
  pays_arr  VARCHAR(42)
);