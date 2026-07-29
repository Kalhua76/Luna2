# LLMProvider

Le composant `LLMProvider` définit le contrat commun que devront respecter
tous les fournisseurs de modèles de langage.

## Objectifs

- Uniformiser l'accès aux différents modèles.
- Découpler Luna des implémentations spécifiques.
- Préparer l'intégration d'OpenAI, Ollama et d'autres fournisseurs.
