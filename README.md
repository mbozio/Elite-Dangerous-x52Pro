# Elite Dangerous X52 Pro Mapper

Prototype d'application de bureau pour visualiser, importer, modifier et exporter des profils `.binds` Elite Dangerous pour HOTAS Logitech/Saitek X52 Pro.

## Objectifs

- Visualiser les axes, boutons, hats et modes du X52 Pro.
- Importer et exporter des fichiers `.binds` directement utilisables dans Elite Dangerous.
- Proposer des assignations rapides intelligentes pour les contrôles directionnels.
- Conserver un historique de décisions projet dans `CONTEXT.md`.

## Démarrage rapide

```bash
PYTHONPATH=src python -m edx52mapper.app
```

ou après installation editable :

```bash
pip install -e .
ed-x52-mapper
```

## Tests

```bash
python -m pytest
```

## Structure

- `src/edx52mapper/binds.py` : parsing/export XML `.binds`.
- `src/edx52mapper/hotas.py` : modèle Logitech X52 Pro.
- `src/edx52mapper/quick_assign.py` : assistants d'assignation rapide.
- `src/edx52mapper/app.py` : prototype d'interface Tkinter.
- `SPECIFICATIONS.md` : spécifications fonctionnelles.
- `PLAN_ACTION.md` : plan d'action et améliorations.
- `CONTEXT.md` : contexte vivant à lire au début de chaque itération.
