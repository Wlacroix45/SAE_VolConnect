SELECT v.id_vol AS vol_id,
       t.poste AS employe_poste,
       COUNT(*) AS nb_employes
FROM vol v,
     TABLE(v.equipage) t
GROUP BY v.id_vol, t.poste;


SELECT t.nom AS employe_nom, 
       t.poste AS employe_poste,
       COUNT(t.nom) AS nb_vols
FROM vol v,
    TABLE(v.equipage) t
WHERE t.poste='Pilote'
GROUP BY t.nom, t.poste;