-- Ce fichier est le fichier contenant les requêtes de la 3.1

-- Donner les villes que nous pouvons atteindre par vols directs en partant de Paris

WITH RECURSIVE vol_dispo AS (
    SELECT
        v.id_vol,
        v.nom_vol,

        v.nom_terminal,

        v.date_heure_depart,
        0 as niveau
    FROM vol v

    UNION ALL

    SELECT 
        v.id_vol,
        v.nom_vol,

        v.nom_terminal,

        v.date_heure_depart,
        ac.niveau + 1
    FROM vol v
    JOIN vol_dispo ac
        ON v.id_vol = ac.id_vol
)
SELECT *
FROM vol_dispo;

WITH RECURSIVE arbre_categories AS (
    -- Niveau 0 : racine
    SELECT
        c.id_categorie,
        c.nom,
        c.id_parent,
        0 AS niveau
    FROM categorie c
    WHERE c.id_categorie = 1   -- catégorie de départ

    UNION ALL

    -- Niveaux suivants : enfants des nœuds déjà trouvés
    SELECT
        c.id_categorie,
        c.nom,
        c.id_parent,
        ac.niveau + 1
    FROM categorie c
    JOIN arbre_categories ac
      ON c.id_parent = ac.id_categorie
)
SELECT *
FROM arbre_categories
ORDER BY niveau, id_categorie;


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