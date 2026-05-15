# Spécifications fonctionnelles

## Vision
L'application doit permettre de concevoir et maintenir des profils de contrôles Elite Dangerous pour HOTAS Logitech X52 Pro sans éditer manuellement les fichiers `.binds`.

## Utilisateurs cibles
- Joueurs Elite Dangerous possédant un Logitech/Saitek X52 Pro.
- Joueurs souhaitant comprendre visuellement leurs assignations.
- Joueurs souhaitant sauvegarder, partager, importer et exporter rapidement plusieurs profils.

## Exigences principales

### Import/export `.binds`
- Importer un fichier `.binds` existant.
- Conserver les commandes, attributs et éléments XML non modifiés autant que possible.
- Exporter un fichier `.binds` directement utilisable par Elite Dangerous.
- Proposer une sauvegarde dans un dossier utilisateur dédié.
- Préparer l'écriture vers le dossier de bindings du jeu quand il sera configuré.

### Visualisation HOTAS
- Afficher les axes sous forme de sliders.
- Afficher les boutons sous forme de voyants visuels.
- Afficher les hats comme des contrôles directionnels haut/droite/bas/gauche.
- Distinguer les modes du X52 Pro.
- Prévoir des visuels réalistes lorsque cela reste maintenable et adapté.

### Édition de commandes
- Permettre de lier une action du jeu à un axe, un bouton ou une direction de hat.
- Retrouver facilement les modes de configuration de chaque commande : axe, maintien, bascule, inversion, deadzone et combinaison.
- Montrer clairement si une commande est non assignée, assignée une fois ou assignée plusieurs fois.

### Assignations rapides intelligentes
- Assigner automatiquement un hat complet vers quatre commandes directionnelles cohérentes.
- Exemple : `Hat 1` vers regarder haut/droite/bas/gauche.
- Exemple : `Hat 2` haut/bas vers propulseurs verticaux.
- Réduire les erreurs en affichant un aperçu avant application.

## Contraintes techniques
- Application légère pour PC.
- Accès en lecture/écriture aux fichiers utilisateur.
- Accès configurable au répertoire de bindings Elite Dangerous.
- Tests automatisés pour le parsing/export et les assistants.

## Hors périmètre initial
- Pilotage direct du jeu en temps réel.
- Capture matérielle avancée du X52 Pro sans validation d'une bibliothèque multiplateforme.
- Téléchargement automatique de profils depuis Internet.
