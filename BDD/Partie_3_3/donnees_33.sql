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
  equipage,
  indices_qualite
) VALUES (
  'V001',
  'Vol Paris-Londres',
  '1',
  '2',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 3, 4),
    indice_qualite('securite', 2, 4),
    indice_qualite('prix', 3, 3)
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
  equipage,
  indices_qualite
) VALUES (
  'V002',
  'Vol Paris-New York',
  '3',
  '4',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 4, 3),
    indice_qualite('securite', 3, 4),
    indice_qualite('prix', 2, 3)
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
  equipage,
  indices_qualite
) VALUES (
  'V003',
  'Vol London-Tokyo',
  '5',
  '6',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 4, 4),
    indice_qualite('securite', 3, 5),
    indice_qualite('prix', 2, 2)
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
  equipage,
  indices_qualite
) VALUES (
  'V004',
  'Vol Berlin-Madrid',
  '7',
  '8',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 2, 3),
    indice_qualite('securite', 2, 4),
    indice_qualite('prix', 3, 4)
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
  equipage,
  indices_qualite
) VALUES (
  'V005',
  'Vol Rome-Amsterdam',
  '9',
  '10',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 3, 3),
    indice_qualite('securite', 3, 5),
    indice_qualite('prix', 3, 4)
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
  equipage,
  indices_qualite
) VALUES (
  'V006',
  'Vol Sydney-Singapore',
  '11',
  '12',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 3, 4),
    indice_qualite('securite', 2, 4),
    indice_qualite('prix', 3, 4)
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
  equipage,
  indices_qualite
) VALUES (
  'V007',
  'Vol Dubai-Cairo',
  '13',
  '14',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 3, 4),
    indice_qualite('securite', 3, 5),
    indice_qualite('prix', 3, 4)
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
  equipage,
  indices_qualite
) VALUES (
  'V008',
  'Vol Toronto-Vancouver',
  '15',
  '16',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 2, 3),
    indice_qualite('securite', 2, 4),
    indice_qualite('prix', 3, 4)
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
  equipage,
  indices_qualite
) VALUES (
  'V009',
  'Vol Mexico City-Lima',
  '17',
  '18',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 3, 4),
    indice_qualite('securite', 2, 4),
    indice_qualite('prix', 3, 3)
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
  equipage,
  indices_qualite
) VALUES (
  'V010',
  'Vol Sao Paulo-Buenos Aires',
  '19',
  '20',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 3, 3),
    indice_qualite('securite', 2, 4),
    indice_qualite('prix', 2, 3)
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
  equipage,
  indices_qualite
) VALUES (
  'V011',
  'Vol Mumbai-Delhi',
  '21',
  '22',
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
  ),
  indice_qualite_tab(
    indice_qualite('carbone', 2, 3),
    indice_qualite('securite', 3, 4),
    indice_qualite('prix', 3, 4)
  )
);