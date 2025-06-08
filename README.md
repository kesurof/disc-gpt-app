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

## 💰 Estimations de coût API (OpenAI)

| Modèle         | Coût estimé par test complet | Tokens estimés          | Remarques              |
|----------------|------------------------------|--------------------------|-------------------------|
| gpt-3.5-turbo  | ~0.0075 $                    | ~1 500 in / 4 000 out    | Économique, rapide      |
| gpt-4-turbo    | ~0.1350 $                    | ~1 500 in / 4 000 out    | Meilleure qualité       |

> 💡 L’estimation est affichée automatiquement dans l’interface avant génération.

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

