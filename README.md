# 🧠 Test DISC avec GPT (Streamlit + OpenAI)

Cette application Streamlit utilise l'API d'OpenAI pour générer des questionnaires DISC aléatoires, analyser les réponses, et proposer une synthèse de votre profil comportemental (Dominance, Influence, Stabilité, Conformité).

---

## 🔍 Objectif

Le test DISC est un outil de compréhension des comportements humains. Cette application permet de :
- Générer dynamiquement un questionnaire DISC personnalisé
- Mémoriser les réponses sans biais (ordre aléatoire)
- Analyser les tendances de comportement
- Produire un résumé interprétatif automatique basé sur le modèle DISC

---

## 🚀 Fonctionnalités

- Génération aléatoire de 10 à 28 questions DISC
- Réponses mélangées automatiquement (anti-biais)
- Analyse automatisée des styles DISC (D/I/S/C)
- Synthèse textuelle du profil avec conseils personnalisés
- Estimation dynamique des coûts API
- Choix du contexte (pro/perso/équipe) et du niveau de langage

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

## 🧪 Exemple d'utilisation

1. Sélectionnez le **contexte** : Professionnel, Personnel ou Équipe
2. Choisissez le **niveau de langage** : Grand public, Étudiant, Manager
3. Lancez la génération du questionnaire
4. Répondez aux questions proposées
5. Cliquez sur **Analyser mes réponses**
6. Obtenez le résultat DISC avec recommandations

---

## 💰 Estimation des coûts API (OpenAI)

| Modèle            | Prix (entrée / sortie) | Estimation pour un test | Remarques                         |
|-------------------|------------------------|--------------------------|-----------------------------------|
| `gpt-3.5-turbo`   | 0,5 ¢ / 1,5 ¢ par 1K tokens | ~0,0068 $ | Économique, suffisant pour usage standard |
| `gpt-4o`          | 2,5 ¢ / 10 ¢ par 1K tokens  | ~0,0438 $ |Rapide, économique, haute qualité |

> Estimation calculée sur une base de ~1500 tokens en entrée et ~4000 en sortie.

---

## 🔐 Respect de la vie privée

Aucune donnée n’est stockée. Toutes les interactions se font directement entre votre navigateur, Streamlit et l’API OpenAI. Les réponses ne sont ni conservées, ni partagées.

---

## 🗂 Structure du projet

```
disc-gpt-app/
├── app.py                     # Script principal Streamlit
├── .streamlit/
│   └── config.toml            # Configuration de l'interface
├── requirements.txt           # Dépendances Python
├── README.md                  # Documentation du projet
└── docs/
```

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

## ❓ FAQ

**Q : Est-ce que ce test est scientifiquement validé ?**  
R : Le modèle DISC est reconnu, mais ce test est généré par IA, donc non validé cliniquement.

**Est-ce que GPT-3.5 suffit ?**  
Oui, il fonctionne bien pour l’analyse. GPT-4 est recommandé si tu veux des textes plus nuancés.

**Q : Puis-je utiliser cela sans compte OpenAI ?**  
R : Non. Une clé API personnelle OpenAI est requise.

**Puis-je utiliser ce projet sans carte bancaire ?**  
Non. OpenAI exige un paiement minimal ou une carte enregistrée pour débloquer l’accès API.

**Q : Les résultats sont-ils enregistrés ?**  
R : Non. Tout est temporaire et traité uniquement côté utilisateur.

---

## 👨‍💻 Auteur

Ce projet a été conçu pour :

- automatiser la création et l'analyse de tests DISC,
- garantir une neutralité dans les réponses,
- proposer une interface simple, sans base de données.

**Technos** : Python · Streamlit · OpenAI API

> Libre d'utilisation pour usage personnel, professionnel ou pédagogique.
