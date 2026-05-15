# AGENTS.md

## Projet
Application de bureau légère pour créer, visualiser, importer et exporter des profils `.binds` Elite Dangerous pour HOTAS Logitech/Saitek X52 Pro.

## Règles de travail obligatoires
- Lire `CONTEXT.md` au début de chaque nouvelle demande avant de modifier le dépôt.
- Mettre à jour `CONTEXT.md` à chaque itération avec l'état courant, les décisions et les prochaines étapes.
- Maintenir `SPECIFICATIONS.md` comme source de vérité fonctionnelle.
- Maintenir `PLAN_ACTION.md` avec le plan, les priorités et les idées d'amélioration.
- Développer hors de `main`, dans une branche de suivi dédiée.

## Style et conventions
- Langue des documents produit : français.
- Code Python : typage explicite quand c'est pertinent, fonctions petites, logique métier séparée de l'interface.
- Éviter les dépendances lourdes tant que la fonctionnalité peut être fournie par la bibliothèque standard.
- Les fichiers `.binds` manipulés par l'application doivent rester directement utilisables par Elite Dangerous.

## Tests
- Ajouter des tests automatisés pour la logique de parsing/export et les assistants d'assignation.
- Ne pas dépendre d'un jeu installé pour exécuter les tests.
