SELECT t.nom AS employe_nom, 
       t.poste AS employe_poste
FROM vol v,
     TABLE(v.equipage) t
ORDER BY t.poste;