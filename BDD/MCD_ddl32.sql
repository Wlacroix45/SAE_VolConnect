DROP TABLE vol;
DROP TYPE employe_tab;
DROP TYPE employe;

CREATE OR REPLACE TYPE employe AS OBJECT (
  nom VARCHAR2(20),
  poste VARCHAR2(20)
);
/
CREATE OR REPLACE TYPE employe_tab AS TABLE OF employe;
/
CREATE TABLE vol (
  id_vol             VARCHAR2(42) NOT NULL,
  nom_vol            VARCHAR2(42),
  date_heure_depart  VARCHAR2(42),
  date_heure_arrivee VARCHAR2(42),
  nom_comp           VARCHAR2(42),
  nom_terminal       VARCHAR2(42),
  ville              VARCHAR2(42),
  pays               VARCHAR2(42),
  equipage           employe_tab,
  PRIMARY KEY (id_vol)
) NESTED TABLE equipage STORE AS equipage_nt;
