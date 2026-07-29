# Luna Runtime – Point d'entrée officiel

## Point d'entrée

Le point d'entrée officiel de Luna Runtime est :

```
main.py
```

Il instancie :

```
LunaRuntime
```

situé dans :

```
src/luna/runtime.py
```

## Chaîne de démarrage

```
main.py
    ↓
LunaRuntime
    ↓
ServiceContainer
    ↓
LunaKernel
```

## Fichiers historiques

Les fichiers suivants sont conservés temporairement pour compatibilité ou migration :

* `bootstrap.py`
* `run.py`

Ils ne doivent plus être utilisés comme point d'entrée principal.

Toute nouvelle fonctionnalité devra être intégrée à partir de `main.py`.
