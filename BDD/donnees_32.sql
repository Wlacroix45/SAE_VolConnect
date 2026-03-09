INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal,
  ville,
  pays,
  equipage
) VALUES (
  'V001',
  'Vol Paris-Londres',
  '2026-03-10 08:00',
  '2026-03-10 09:30',
  'AirFrance',
  'Terminal 2',
  'Paris',
  'France',
  employe_tab(
    employe('Dupont', 'Pilote'),
    employe('Martin', 'Copilote'),
    employe('Durand', 'Hôtesse')
  )
);