# 🧠 Test DISC avec GPT (Streamlit + OpenAI)

Cette application permet de générer un **questionnaire DISC personnalisé** et d’analyser automatiquement les réponses pour déterminer le **profil comportemental DISC** d’un utilisateur (Dominance, Influence, Stabilité, Conformité).

---

## ✅ Fonctionnalités

- Génération dynamique de 10 à 28 questions DISC
- Formulation neutre, sans biais de position
- Analyse automatique par IA (profil dominant, secondaire, synthèse)
- Estimation du coût API selon le modèle utilisé
- Interface web déployable gratuitement via Streamlit Cloud

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

2. Il génère le **questionnaire DISC** et répond à chaque question dans l’interface.

3. Il obtient :
   - Une **répartition des réponses** par profil
   - Une **couleur dominante et secondaire**
   - Une **synthèse comportementale personnalisée**
   - Des **recommandations ciblées**

---

## 💰 Estimations de coût API (OpenAI)

| Modèle         | Coût estimé par test complet | Tokens estimés          | Remarques              |
|----------------|------------------------------|--------------------------|-------------------------|
| gpt-3.5-turbo  | ~0.0075 $                    | ~1 500 in / 4 000 out    | Rapide, économique      |
| gpt-4-turbo    | ~0.1350 $                    | ~1 500 in / 4 000 out    | Analyse plus détaillée  |

> 💡 L’estimation du coût est affichée dynamiquement dans l’interface avant chaque génération.

---

## 🛡️ Respect de la vie privée

- Aucune donnée personnelle n’est stockée.
- Les réponses sont temporairement envoyées à l’API OpenAI pour traitement.
- Aucun cookie, tracking ou base de données.
- L’interface fonctionne uniquement côté client + API.

---

## 🚀 Déploiement rapide via Streamlit Cloud

### Étapes :

1. Clone ou importe ce dépôt sur ton GitHub.
2. Connecte-toi à [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Crée une **nouvelle application**.
4. Renseigne :
   - Nom du dépôt GitHub
   - Fichier principal : `app.py`
5. Dans **“Advanced settings”** > **“Secrets”**, ajoute :

```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"

📁 Structure du projet
bash
Copier
Modifier
disc-gpt-app/
├── app.py               ← Interface principale Streamlit
├── requirements.txt     ← Dépendances Python (Streamlit + OpenAI)
└── README.md            ← Document de présentation du projet
❓ FAQ
Est-ce que GPT-3.5 suffit pour ce type d’analyse ?
Oui. GPT-3.5 fournit des résultats corrects et économiques. GPT-4 est recommandé pour une synthèse plus fluide.

Puis-je utiliser cette app sans carte bancaire ?
Non. OpenAI exige une activation de facturation même pour les faibles montants (ex. : 5 $ prépayés).

Est-ce que je peux déployer l’app ailleurs ?
Oui. Tu peux exécuter ce projet localement (streamlit run app.py) ou l’intégrer dans un conteneur Docker, sur un VPS, etc.

Le projet stocke-t-il des données utilisateurs ?
Non. Toutes les interactions sont jetables. Les réponses sont traitées en mémoire et transmises uniquement à l’API OpenAI.

👨‍💻 Auteur
Ce projet a été conçu pour :

démocratiser l’accès au modèle DISC via IA,

automatiser les évaluations comportementales,

permettre un usage sans infrastructure ni base de données.

Tu peux l’utiliser pour :

des bilans RH internes,

du coaching personnel ou d’équipe,

des formations sur la connaissance de soi,

des applications pédagogiques.

Technologies utilisées :

Python 3

Streamlit

OpenAI GPT (3.5 & 4-turbo)

📬 Contributions
Toute suggestion, amélioration ou bug peut être soumis via une issue ou une pull request.