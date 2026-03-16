SELECT t.nom AS employe_nom, 
       t.poste AS employe_poste
FROM vol v,
     TABLE(v.equipage) t
ORDER BY t.poste;


SELECT t.nom AS employe_nom, 
       t.poste AS employe_poste,
       COUNT(t.nom) AS nb_vols
FROM vol v,
    TABLE(v.equipage) t
WHERE t.poste='Pilote'
GROUP BY t.nom, t.poste;