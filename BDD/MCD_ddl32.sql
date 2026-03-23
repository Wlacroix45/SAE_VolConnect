DROP TABLE vol;
DROP TYPE employe_tab;
DROP TYPE employe;
DROP TYPE indice_qualite_tab;
DROP TYPE indice_qualite;

CREATE OR REPLACE TYPE employe AS OBJECT (
  nom VARCHAR2(20),
  poste VARCHAR2(20)
);
/
CREATE OR REPLACE TYPE employe_tab AS TABLE OF employe;
/
CREATE OR REPLACE TYPE indice_qualite AS OBJECT (
  nom_indice VARCHAR2(20),
  poids NUMBER(3,1)
);
/
CREATE OR REPLACE TYPE indice_qualite_tab AS TABLE OF indice_qualite;
/
CREATE TABLE vol (
  id_vol             VARCHAR2(42) NOT NULL,
  nom_vol            VARCHAR2(42),
  date_heure_depart  VARCHAR2(42),
  date_heure_arrivee VARCHAR2(42),
  nom_comp           VARCHAR2(42),
  nom_terminal_depart       VARCHAR2(42),
  nom_terminal_arrivee       VARCHAR2(42),
  ville_depart       VARCHAR2(42),
  ville_arrivee       VARCHAR2(42),
  pays_depart               VARCHAR2(42),
  pays_arrivee               VARCHAR2(42),
  equipage           employe_tab,
  indices_qualite    indice_qualite_tab,
  PRIMARY KEY (id_vol)
) NESTED TABLE equipage STORE AS equipage_nt
  NESTED TABLE indices_qualite STORE AS indices_qualite_nt;
