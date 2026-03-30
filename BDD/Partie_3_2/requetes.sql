-- Pour chaque vol, donner le nombre de personnes de l’équipage, par fonction
SELECT v.id_vol AS vol_id,
       t.poste AS employe_poste,
       COUNT(*) AS nb_employes
FROM vol v,
     TABLE(v.equipage) t
GROUP BY v.id_vol, t.poste;

-- Pour chaque pilote, indiquer combien des vols lui sont associés
SELECT t.nom AS employe_nom, 
       t.poste AS employe_poste,
       COUNT(t.nom) AS nb_vols
FROM vol v,
    TABLE(v.equipage) t
WHERE t.poste='Pilote'
GROUP BY t.nom, t.poste;

-- Pour chaque vol, donner l’impact de chaque indice de qualité (valeur * poids)
SELECT v.id_vol AS vol_id,
       i.nom_indice AS indice_nom,
       (i.valeur * i.poids) AS impact
FROM vol v,
     TABLE(v.indices_qualite) i;

Select v.id_vol AS vol_id,

-- Pour chaque indice de qualité, calculer son impact moyen       
SELECT i.nom_indice AS indice_nom,
       ROUND(AVG(i.valeur * i.poids), 3) AS impact_moyen
FROM vol v,
     TABLE(v.indices_qualite) i
GROUP BY i.nom_indice;