# 🧠 Test DISC avec GPT (Streamlit + OpenAI)

Cette application permet de générer un **questionnaire DISC personnalisé** et d’analyser automatiquement les réponses pour déterminer le **profil comportemental DISC** d’un utilisateur (Dominance, Influence, Stabilité, Conformité).

---

## ✅ Fonctionnalités

- Génération dynamique de 10 à 28 questions DISC
- Ordre des réponses totalement aléatoire à chaque question
- Réponses **sans lettres visibles (A/B/C/D)** pour éviter le biais
- Analyse automatique par IA (profil dominant, secondaire, synthèse)
- Estimation du coût API selon le modèle sélectionné
- Interface web prête à déployer via Streamlit Cloud

---

## 📦 Prérequis

- Un compte [GitHub](https://github.com)
- Un compte [Streamlit Cloud](https://streamlit.io/cloud)
- Un compte [OpenAI](https://platform.openai.com) avec :
  - Clé API valide (`sk-...`)
  - Paiement activé (crédit prépayé ou carte bancaire)

---

## ⚙️ Options de configuration

### 🎯 Contexte

Le contexte sélectionné influence la formulation des questions DISC.

| Contexte      | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **Professionnel** | Questions orientées vers les situations de travail, gestion, performance |
| **Personnel**     | Questions centrées sur les préférences et comportements individuels       |
| **Équipe**        | Questions axées sur la collaboration, le collectif et les dynamiques de groupe |

---

### ✏️ Niveau de langage

Le niveau de langage adapte la complexité du vocabulaire utilisé.

| Niveau             | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| **Grand public**   | Formulation simple, accessible à tous, sans jargon                       |
| **Étudiant**       | Ton neutre, explicite, avec un vocabulaire courant mais structuré        |
| **Manager**        | Style plus formel, professionnel, adapté à un public encadrant ou cadre  |

---

## 💡 Exemple d'utilisation

1. L'utilisateur choisit :
   - Le **contexte** (professionnel, personnel…)
   - La **langue**
   - Le **niveau de langage**
   - Le **nombre de questions**
   - Le **modèle GPT** (`gpt-3.5-turbo` ou `gpt-4-turbo`)

2. Il génère un **questionnaire DISC aléatoire** :
   - Chaque réponse est affichée sans lettre visible.
   - Les styles DISC (D/I/S/C) sont cachés via un marquage `::X`.

3. L’utilisateur répond sans savoir à quel type chaque réponse correspond.

4. À la fin, l'application :
   - Compte les styles choisis,
   - Détermine le profil DISC (dominant + secondaire),
   - Génère une synthèse descriptive + conseils.

---

## 💰 Estimation des coûts API (OpenAI)

L'application fonctionne avec plusieurs modèles OpenAI compatibles avec les fonctions `chat.completions`.

| Modèle             | Coût estimé par test complet | Tarif (approx. input/output)     | Remarques                         |
|--------------------|------------------------------|-----------------------------------|-----------------------------------|
| gpt-3.5-turbo      | ~0.0075 $                    | $0.0005 / $0.0015 par 1k tokens   | Économique, suffisant pour usage standard |
| gpt-4-turbo        | ~0.1350 $                    | $0.01 / $0.03 par 1k tokens       | Meilleure qualité d’analyse       |
| gpt-4o             | ~0.0450 $                    | $0.005 / $0.015 par 1k tokens     | Rapide, économique, haute qualité |
| gpt-4.5-preview    | ~0.0900 $                    | Estimé proche de gpt-4-turbo      | À confirmer selon ton plan        |

> Le coût exact dépend du nombre de tokens échangés (texte envoyé + réponse générée).
> L’estimation est automatiquement affichée dans l’interface selon le modèle sélectionné.

---

### 📐 Méthode de calcul interne

- **Tokens estimés** :
  - ≈ 1 500 pour la génération du questionnaire
  - ≈ 4 000 pour l’analyse des réponses
- **Formule appliquée** :
````
(input_tokens / 1000) × input_cost + (output_tokens / 1000) × output_cost
````

Ces valeurs sont utilisées pour afficher une **estimation dynamique** dans l’application avant chaque génération.

---

## 🛡️ Respect de la vie privée

- Aucune donnée personnelle n’est enregistrée.
- Les réponses sont traitées uniquement côté client, puis via l’API OpenAI.
- Aucune base de données, aucun cookie, aucune traçabilité.

---

## 🚀 Déploiement rapide via Streamlit Cloud

### Étapes :

1. Clone ou importe ce dépôt sur ton GitHub.
2. Connecte-toi à [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Crée une **nouvelle application**.
4. Renseigne :
   - Nom du dépôt GitHub
   - Fichier principal : `app.py`
5. Dans **Advanced settings > Secrets**, ajoute :

```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
```

6. Clique sur **Deploy**.

---

## 📁 Structure du projet

<details>
<summary>📁 Structure du projet</summary>

disc-gpt-app/
├── app.py ← Interface principale Streamlit
├── requirements.txt ← Dépendances Python (Streamlit + OpenAI)
├── README.md ← Documentation du projet
└── .streamlit/
└── config.toml ← (optionnel) Configuration visuelle Streamlit (thème, layout, etc.)


</details>

---

## ❓ FAQ

**Pourquoi les lettres A/B/C/D ont été supprimées ?**  
Pour éviter que l’utilisateur repère les styles DISC à travers la position ou répétition. L’ordre est désormais mélangé et invisible.

**Est-ce que GPT-3.5 suffit ?**  
Oui, il fonctionne bien pour l’analyse. GPT-4 est recommandé si tu veux des textes plus nuancés.

**Puis-je utiliser ce projet sans carte bancaire ?**  
Non. OpenAI exige un paiement minimal ou une carte enregistrée pour débloquer l’accès API.

**Puis-je utiliser cette app hors ligne ?**  
Non. L’analyse dépend de l’appel API à OpenAI. Tu peux l’héberger localement, mais l’API reste nécessaire.

---

## 👨‍💻 Auteur

Ce projet a été conçu pour :

- automatiser la création et l'analyse de tests DISC,
- garantir une neutralité dans les réponses,
- proposer une interface simple, sans base de données.

**Technos** : Python · Streamlit · OpenAI API

> Libre d'utilisation pour usage personnel, professionnel ou pédagogique.

