# Sae VolConnect

Membres de groupe :

Chef de projet : PUPP--BAUDSON Gwendan

Gestionnaire Git : LACROIX Wyatt

Contrôleur de qualité : GUERRIER Titouan

## Démonstration

Vous avez à disposition une vidéo de démonstration, qui montre le fonctionnement de la SPA et de l'application mobile. Elle est accessible depuis le lien suivant :
- https://youtu.be/1mcJ-enVnOw

## Prérequis

- Vous devez avoir installé python 
- Vous devez pouvoir lancer un serveur local (Ex: php)
- Vous devez avoir installé flutter et dart à minimat (mieux avec Android studio)
- Il faut un dossier sdk

## Lancement Serveur API

Avant de vouloir lancer la SPA ou l'application mobile, vous devez lancer le serveur de l'API.
Tout d'abord, vous devez créer un environnement virtuel et installer toutes les dépendances. Pour ce faire, mettez vous à la racine du projet (SAE_VolConnect/) et tapez les commandes suivantes :
- virtualenv -p python3 venv
- source venv/bin/activate
- pip install -r requirements.txt
  
Vous aurez alors installé toutes les dépendances nécessaires pour utiliser les commandes flask nécessaires au lancement du serveur. Pour le lancer, vous devez charger les jeux de données avant de lancer le serveur (à faire qu'une seule fois, avant le premier démarrage):
- flask syncdb (toujours à la racine du projet)

Enfin, vous pouvez lancer le serveur avec la commande suivante :
- flask run

Pour lancer les tests coverage de l'API REST vous devez aller dans le dossier vol/
- cd vol/

Puis lancez les tests:
- coverage run -m pytest

Pour générer les résulats: 
- coverage report -m

Vous pouvez en générer une page HTML:
- coverage HTML (Dossier htmlcov créé dans le dossier vol/)
- Ouvir le fichier index.html sur votre navigateur

## Lancement SPA

Une fois le serveur lancé, vous pourrez alors lancer la SPA. Pour cela dirigez vous vers le dossier SPA :
- cd SPA/

Puis, lancez un serveur local :
- Exemple avec php : php -S localhost:8000

Sur votre navigateur, en mettant comme URL http://localhost:8000/ vous accéderez à la SPA et pourrez effectuez toutes les actions que vous souhaitez (cf Manuel Utilisateur présent dans le dossier Livrable/)

## Lancement Application Mobile
Pour lancer l'application, il faut lancer un terminal et vous dirigez vers le dossier android : 
- cd dev_mobile/

Vous pourrez alors lancer l'application Web
- flutter run -d chrome 

Si ça marche pas :
- flutter run <"votre navigateur">


