#
# AI Service Architecture  
## Compréhension pratique du fonctionnement réel d’un système IA

---

## Objectif du projet

Ce projet n’a pas pour but de simplement “utiliser” un modèle d’IA.

Il démontre une compréhension **technique, opérationnelle et architecturale** du fonctionnement réel d’un système d’intelligence artificielle déployé comme service.

Beaucoup parlent d’IA.  
Peu comprennent réellement :

- Comment on appelle un modèle
- Comment fonctionne l’inférence
- Comment un modèle devient un service HTTP
- Comment récupérer et analyser une réponse JSON
- Comment débugger un serveur IA

Ce projet répond précisément à ces points.

---

## Architecture du système

Le projet repose sur une architecture moderne orientée service :

LLM (Ollama)  
⬇  
API Backend (FastAPI + Uvicorn)  
⬇  
Exposition HTTP  
⬇  
Client (curl / navigateur)  

---

## Résumé technique

Ce projet démontre une compréhension **pratique et moderne** du fonctionnement réel d’un système d’intelligence artificielle déployé localement.

Plutôt que d’utiliser une API distante, l’objectif était de maîtriser l’architecture complète :

- Déploiement d’un modèle LLM en local (Ollama)
- Exposition via une API REST (FastAPI + Uvicorn)
- Communication HTTP
- Manipulation et analyse de réponses JSON
- Debug et analyse des logs serveur
- Gestion des processus et ports réseau
- Conteneurisation avec Docker

Ce projet montre que :

- Un modèle d’IA fonctionne comme un service réseau
- L’inférence est un processus backend observable
- L’IA s’intègre dans une architecture moderne (API-first)
- Les logs, ports et processus sont essentiels à la compréhension du système

---

## Stack moderne utilisée

- Arch Linux (environnement virtualisé)
- FastAPI (framework backend moderne)
- Uvicorn (serveur ASGI)
- Ollama (LLM local)
- Docker (conteneurisation)
- curl (validation HTTP et tests d’API)

---

## 🔐 Perspective Sécurité

La compréhension technique acquise à travers ce projet constitue une base solide pour évoluer vers :

- AI Security
- LLM Security
- Prompt Injection Analysis
- AI Red Teaming

Comprendre comment un modèle est exposé, interrogé et intégré dans un service backend est une étape essentielle avant toute analyse de sécurité avancée.

---

## ✅ Conclusion

Ce projet ne se limite pas à “utiliser” un modèle.

Il démontre une compréhension réelle de son fonctionnement en environnement technique moderne.
