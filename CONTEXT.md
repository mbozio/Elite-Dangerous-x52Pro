# Contexte de suivi

## État initial
- Dépôt GitHub nouvellement créé, sans application existante.
- Branche `main` conservée comme base stable.
- Développement initial effectué dans la branche `feature/bootstrap-hotas-mapper`.

## Objectif produit
Créer une application de bureau légère pour PC permettant à un joueur Elite Dangerous équipé d'un HOTAS Logitech X52 Pro de :
- visualiser les axes, boutons, hats et modes du HOTAS ;
- importer des profils Elite Dangerous `.binds` ;
- éditer et exporter des profils `.binds` directement utilisables dans le jeu ;
- sauvegarder des profils dans un dossier utilisateur ;
- proposer des assignations rapides intelligentes, par exemple un hat complet vers les commandes haut/droite/bas/gauche d'une même fonction.

## Décisions techniques
- Langage retenu : Python 3.11+, car il est adapté à une application légère, portable, testable, avec accès simple au système de fichiers utilisateur et aux dossiers du jeu.
- Interface initiale : Tkinter, inclus dans la bibliothèque standard, pour éviter une dépendance lourde au démarrage du projet.
- Architecture : logique `.binds` indépendante de l'interface pour faciliter les tests et une future migration éventuelle vers PySide6/Qt si des visuels plus avancés sont nécessaires.

## Fonctionnalités amorcées
- Modèle de commandes HOTAS X52 Pro avec axes, boutons, hats et modes.
- Parsing XML générique des fichiers `.binds` Elite Dangerous.
- Export XML compatible avec l'import jeu en conservant la structure chargée.
- Assistant d'assignation rapide d'un hat vers 4 actions directionnelles.
- Prototype d'interface visuelle avec sliders d'axes, voyants de boutons et hats cliquables.

## Prochaines étapes
- Ajouter une détection plus robuste des dossiers Elite Dangerous selon Windows/Steam/Epic/Frontier.
- Ajouter un rendu visuel plus réaliste du joystick et de la manette des gaz.
- Ajouter un éditeur détaillé des modes de commande : axe, maintien, bascule, inversion, deadzone, courbe, combinaison.
- Ajouter un assistant dédié aux propulseurs verticaux/latéraux et à la direction de vue.
- Valider l'export avec des fichiers `.binds` réels fournis par un utilisateur.
