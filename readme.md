# Sae VolConnect

Membres de groupe :

Chef de projet : PUPP--BAUDSON Gwendan

Gestionnaire Git : LACROIX Wyatt

Contrôleur de qualité : GUERRIER Titouan



## commande ora12

rlwrap sqlplus nom@ora12

si c'est votre première fois le mdp est votre nom

pour supprimer toutes les tables indésirables utiliser la commande @./BDD/dropAll.sql .

ensuite il faut vider la corbeille avec purge recyclebin; 

et pour lancer le script sql @./BDD/MCD_ddl32.sql et @./BDD/donnees_32.sql

- virtualenv -p python3 venv
- source venv/bin/activate
- pip install -r requirements.txt
- flask run 
- flask run --debug
