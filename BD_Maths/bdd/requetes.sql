-- Ce fichier est le fichier contenant les requêtes de la 3.1

-- Donner les villes que nous pouvons atteindre par vols directs en partant de Paris

SELECT DISTINCT ville_arr
FROM vol
WHERE ville_dep = 'Paris'
ORDER BY ville_arr;


-- même question mais avec UNE correspondance

SELECT DISTINCT v2.ville_arr
FROM vol v1
JOIN vol v2 ON v1.ville_arr = v2.ville_dep
  AND STR_TO_DATE(v1.date_heure_arrivee, '%Y-%m-%d %H:%i') 
      < STR_TO_DATE(v2.date_heure_depart, '%Y-%m-%d %H:%i')
WHERE v1.ville_dep = 'Paris'
ORDER BY v2.ville_arr;



-- même question mais avec DEUX correspondances

SELECT DISTINCT v3.ville_arr
FROM vol v1
JOIN vol v2 ON v1.ville_arr = v2.ville_dep
  AND STR_TO_DATE(v1.date_heure_arrivee, '%Y-%m-%d %H:%i') 
      < STR_TO_DATE(v2.date_heure_depart, '%Y-%m-%d %H:%i')
JOIN vol v3 ON v2.ville_arr = v3.ville_dep
  AND STR_TO_DATE(v2.date_heure_arrivee, '%Y-%m-%d %H:%i') 
      < STR_TO_DATE(v3.date_heure_depart, '%Y-%m-%d %H:%i')
WHERE v1.ville_dep = 'Paris'
ORDER BY v3.ville_arr;

-- même question mais on ne spécifie pas le nb de correspondance

WITH RECURSIVE trajets AS (
  SELECT ville_arr as destination, date_heure_arrivee as derniere_arrivee, 1 as niveau
  FROM vol
  WHERE ville_dep = 'Paris'
  
  UNION ALL
  
  SELECT v.ville_arr, v.date_heure_arrivee, t.niveau + 1
  FROM trajets t
  JOIN vol v ON t.destination = v.ville_dep
    AND STR_TO_DATE(t.derniere_arrivee, '%Y-%m-%d %H:%i') < STR_TO_DATE(v.date_heure_depart, '%Y-%m-%d %H:%i')
  WHERE t.niveau < 10
)
SELECT DISTINCT destination
FROM trajets
ORDER BY destination;