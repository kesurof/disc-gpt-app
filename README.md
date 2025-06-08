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
5. Dans **Advanced settings > Secrets**, ajoute :

```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
```


6. Clique sur **Deploy**.

---

## 📁 Structure du projet

<details>
<summary>📁 Structure du projet</summary>
```
disc-gpt-app/
├── app.py ← Interface principale Streamlit
├── requirements.txt ← Dépendances Python (Streamlit + OpenAI)
├── README.md ← Documentation du projet
└── .streamlit/
└── config.toml ← (optionnel) Configuration visuelle Streamlit (thème, layout, etc.)
```
</details>

---

## ❓ FAQ

**Est-ce que GPT-3.5 suffit pour ce type d’analyse ?**  
Oui. GPT-3.5 fournit des résultats corrects et économiques. GPT-4 est recommandé pour une synthèse plus fluide.

**Puis-je utiliser cette app sans carte bancaire ?**  
Non. OpenAI exige un premier paiement ou une carte enregistrée, même pour utiliser les modèles les moins chers.

**Puis-je déployer l’app ailleurs ?**  
Oui. Elle fonctionne aussi localement (`streamlit run app.py`), sur un serveur personnel ou en conteneur Docker.

**Le projet stocke-t-il des données utilisateurs ?**  
Non. Toutes les interactions sont jetables. Les données sont uniquement envoyées à l’API, puis perdues.

---

## 👨‍💻 Auteur

Ce projet a été conçu pour :

- démocratiser l’accès au modèle DISC via IA,
- automatiser les évaluations comportementales,
- proposer une interface simple, 100% sans base de données.

**Technologies utilisées** :
- Python 3
- Streamlit
- OpenAI API (`gpt-3.5-turbo`, `gpt-4-turbo`)

> Projet librement réutilisable à but pédagogique, RH ou personnel.
