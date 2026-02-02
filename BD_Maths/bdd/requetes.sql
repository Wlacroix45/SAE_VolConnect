-- Ce fichier est le fichier contenant les requêtes de la 3.1

-- Donner les villes que nous pouvons atteindre par vols directs en partant de Paris
SELECT DISTINCT (id_vol, nom_vol, date_heure_depart) as Vol, (id_aeroport, nom, ville, pays) as Destination_Possible 
FROM vol 
NATURAL JOIN arriver NATURAL JOIN terminal NATURAL JOIN posseder NATURAL JOIN aeroport 
NATURAL JOIN partir
where vol.correspondance = 0
and partir.id_terminal in (select ville from aeroport where ville = 'PARIS');


-- même question mais avec UNE correspondance
SELECT DISTINCT (id_vol, nom_vol, date_heure_depart) as Vol, (id_aeroport, nom, ville, pays) as Destination_Possible 
FROM vol 
NATURAL JOIN arriver NATURAL JOIN terminal NATURAL JOIN posseder NATURAL JOIN aeroport 
NATURAL JOIN partir
where vol.correspondance = 1
and partir.id_terminal in (select ville from aeroport where ville = 'PARIS');


-- même question mais avec DEUX correspondances
SELECT DISTINCT (id_vol, nom_vol, date_heure_depart) as Vol, (id_aeroport, nom, ville, pays) as Destination_Possible 
FROM vol 
NATURAL JOIN arriver NATURAL JOIN terminal NATURAL JOIN posseder NATURAL JOIN aeroport 
NATURAL JOIN partir
where vol.correspondance = 2
and partir.id_terminal in (select ville from aeroport where ville = 'PARIS');

-- même question mais on ne spécifie pas le nb de correspondance
SELECT DISTINCT (id_vol, nom_vol, date_heure_depart) as Vol, (id_aeroport, nom, ville, pays) as Destination_Possible 
FROM vol 
NATURAL JOIN arriver NATURAL JOIN terminal NATURAL JOIN posseder NATURAL JOIN aeroport 
NATURAL JOIN partir
where partir.id_terminal in (select ville from aeroport where ville = 'PARIS');