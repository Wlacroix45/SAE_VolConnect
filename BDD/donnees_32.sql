INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V001',
  'Vol Paris-Londres',
  '2026-03-10 08:00',
  '2026-03-10 09:30',
  'AirFrance',
  'Terminal 2',
  'Terminal 5',
  'Paris',
  'London',
  'France',
  'UK',
  employe_tab(
    employe('Dupont', 'Pilote'),
    employe('Martin', 'Copilote'),
    employe('Durand', 'Hotesse')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V002',
  'Vol Paris-New York',
  '2026-03-20 14:00',
  '2026-03-20 22:00',
  'AirFrance',
  'Terminal 2',
  'Terminal 4',
  'Paris',
  'New York',
  'France',
  'USA',
  employe_tab(
    employe('Leroy', 'Pilote'),
    employe('Bernard', 'Copilote'),
    employe('Petit', 'Hotesse'),
    employe('Roux', 'Steward')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V003',
  'Vol London-Tokyo',
  '2026-04-05 18:00',
  '2026-04-06 12:00',
  'British Airways',
  'Terminal 5',
  'Terminal 2',
  'London',
  'Tokyo',
  'UK',
  'Japan',
  employe_tab(
    employe('Smith', 'Pilote'),
    employe('Johnson', 'Copilote'),
    employe('Williams', 'Hotesse')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V004',
  'Vol Berlin-Madrid',
  '2026-05-12 10:00',
  '2026-05-12 12:30',
  'Lufthansa',
  'Terminal 1',
  'Terminal 4',
  'Berlin',
  'Madrid',
  'Germany',
  'Spain',
  employe_tab(
    employe('Müller', 'Pilote'),
    employe('Schmidt', 'Copilote'),
    employe('Fischer', 'Hotesse'),
    employe('Weber', 'Steward')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V005',
  'Vol Rome-Amsterdam',
  '2026-06-15 09:00',
  '2026-06-15 11:00',
  'Alitalia',
  'Terminal 3',
  'Terminal 2',
  'Rome',
  'Amsterdam',
  'Italy',
  'Netherlands',
  employe_tab(
    employe('Rossi', 'Pilote'),
    employe('Ferrari', 'Copilote'),
    employe('Esposito', 'Hotesse')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V006',
  'Vol Sydney-Singapore',
  '2026-07-22 16:00',
  '2026-07-22 20:00',
  'Qantas',
  'Terminal 1',
  'Terminal 3',
  'Sydney',
  'Singapore',
  'Australia',
  'Singapore',
  employe_tab(
    employe('Brown', 'Pilote'),
    employe('Davis', 'Copilote'),
    employe('Miller', 'Hotesse'),
    employe('Wilson', 'Steward')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V007',
  'Vol Dubai-Cairo',
  '2026-08-10 02:00',
  '2026-08-10 05:00',
  'Emirates',
  'Terminal 3',
  'Terminal 2',
  'Dubai',
  'Cairo',
  'UAE',
  'Egypt',
  employe_tab(
    employe('Al-Farsi', 'Pilote'),
    employe('Al-Mansoori', 'Copilote'),
    employe('Al-Zahra', 'Hotesse')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V008',
  'Vol Toronto-Vancouver',
  '2026-09-18 08:00',
  '2026-09-18 10:30',
  'Air Canada',
  'Terminal 1',
  'Terminal 2',
  'Toronto',
  'Vancouver',
  'Canada',
  'Canada',
  employe_tab(
    employe('Thompson', 'Pilote'),
    employe('Anderson', 'Copilote'),
    employe('Campbell', 'Hotesse'),
    employe('Stewart', 'Steward')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V009',
  'Vol Mexico City-Lima',
  '2026-10-25 12:00',
  '2026-10-25 15:00',
  'Aeromexico',
  'Terminal 2',
  'Terminal 1',
  'Mexico City',
  'Lima',
  'Mexico',
  'Peru',
  employe_tab(
    employe('Garcia', 'Pilote'),
    employe('Rodriguez', 'Copilote'),
    employe('Martinez', 'Hotesse')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V010',
  'Vol Sao Paulo-Buenos Aires',
  '2026-11-30 14:00',
  '2026-11-30 16:30',
  'LATAM',
  'Terminal 3',
  'Terminal A',
  'Sao Paulo',
  'Buenos Aires',
  'Brazil',
  'Argentina',
  employe_tab(
    employe('Silva', 'Pilote'),
    employe('Santos', 'Copilote'),
    employe('Oliveira', 'Hotesse'),
    employe('Pereira', 'Steward')
  )
);

INSERT INTO vol (
  id_vol,
  nom_vol,
  date_heure_depart,
  date_heure_arrivee,
  nom_comp,
  nom_terminal_depart,
  nom_terminal_arrivee,
  ville_depart,
  ville_arrivee,
  pays_depart,
  pays_arrivee,
  equipage
) VALUES (
  'V011',
  'Vol Mumbai-Delhi',
  '2026-12-05 06:00',
  '2026-12-05 07:30',
  'Air India',
  'Terminal 2',
  'Terminal 3',
  'Mumbai',
  'Delhi',
  'India',
  'India',
  employe_tab(
    employe('Patel', 'Pilote'),
    employe('Sharma', 'Copilote'),
    employe('Singh', 'Hotesse')
  )
);