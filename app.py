import streamlit as st
import openai
import random
import re
from collections import Counter

# Initialisation client OpenAI
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

MODELS = {
    "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
    "gpt-4o": {"input": 0.0025, "output": 0.01}
}

def estimer_cout(model, tokens_in, tokens_out):
    p = MODELS[model]
    return round((tokens_in / 1000) * p["input"] + (tokens_out / 1000) * p["output"], 6)

st.set_page_config(page_title="Test DISC", layout="centered")
st.title("🧠 Test DISC – Analyse de profil comportemental")

context = st.selectbox("Contexte", ["Professionnel", "Personnel", "Équipe"])
langue = st.selectbox("Langue", ["Français", "Anglais"])
niveau = st.selectbox("Niveau de langage", ["Grand public", "Étudiant", "Manager"])
nb_questions = st.slider("Nombre de questions", 10, 28, 12)
model = st.selectbox("Modèle GPT utilisé", list(MODELS.keys()))

# Estimation coût
tokens_input = 1500
tokens_output = 4000
estimation = estimer_cout(model, tokens_input, tokens_output)
st.info(f"💰 Estimation du coût API : ~${estimation} pour ce test complet ({model})")

if st.button("Générer le questionnaire"):
    prompt_gen = f'''
Tu es un expert DISC. Génére {nb_questions} questions DISC dans le contexte {context.lower()}, en {langue.lower()}, pour un niveau {niveau.lower()}.

Pour chaque question, propose 4 affirmations. Chaque affirmation doit correspondre exactement à un style DISC :
- Dominance (D)
- Influence (I)
- Stabilité (S)
- Conformité (C)

Ajoute discrètement à la fin de chaque option le style entre double deux-points, exemple : "réponse ici ::D".

Exemple de format :
Q1. Texte de la question ?
- Réponse 1 ::D
- Réponse 2 ::I
- Réponse 3 ::S
- Réponse 4 ::C

Fournis uniquement les questions et réponses, sans explication.
'''
    with st.spinner("Génération en cours..."):
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt_gen}]
        )
    questions_raw = response.choices[0].message.content.strip().split("\n\n")
    st.session_state["questions"] = questions_raw
    st.session_state["options_melangees"] = {}

if "questions" in st.session_state:
    st.markdown("## 📝 Répondez au questionnaire", unsafe_allow_html=True)
    st.markdown('\n<style>\n.question-block {\n  display: flex;\n  flex-wrap: wrap;\n  align-items: flex-start;\n  gap: 1rem;\n  margin-bottom: 1rem;\n}\n\n.question-text {\n  flex: 1 1 250px;\n  font-weight: bold;\n  font-size: 1.1rem;\n  margin-top: 0.5rem;\n}\n\n.answers {\n  flex: 2 1 300px;\n}\n\n@media (max-width: 768px) {\n  .question-block {\n    flex-direction: column;\n  }\n}\n</style>\n', unsafe_allow_html=True)

    if "options_melangees" not in st.session_state:
        st.session_state["options_melangees"] = {}
    responses = []

    for i, bloc in enumerate(st.session_state["questions"]):
        lines = bloc.strip().split("\n")
        if len(lines) < 5:
            continue
        question_text = lines[0]
        options_raw = lines[1:5]

        options_cleaned = []
        for opt in options_raw:
            match = re.search(r"(.*)::([DISC])", opt.strip())
            if match:
                label = match.group(1).strip()
                style = match.group(2)
                options_cleaned.append({"text": label, "style": style})

        if f"q{i}" not in st.session_state["options_melangees"]:
            random.shuffle(options_cleaned)
            st.session_state["options_melangees"][f"q{i}"] = options_cleaned
        else:
            options_cleaned = st.session_state["options_melangees"][f"q{i}"]

        option_labels = [opt["text"] for opt in options_cleaned]

        st.markdown(f"<div class='question-block'><div class='question-text'>Question {i+1} : {question_text.strip()}</div>", unsafe_allow_html=True)
        selection = st.radio(
            label=" ",
            options=option_labels,
            index=None,
            key=f"q{i}",
            label_visibility="collapsed"
        )
        st.markdown("</div><hr>", unsafe_allow_html=True)

        for opt in options_cleaned:
            if opt["text"] == selection:
                responses.append(opt["style"])
                break

    if st.button("Analyser mes réponses"):
        counts = Counter(responses)
        D = counts.get("D", 0)
        I = counts.get("I", 0)
        S = counts.get("S", 0)
        C = counts.get("C", 0)
        prompt_eval = f'''Voici les résultats du questionnaire DISC (nombre de réponses) : D = {D}, I = {I}, S = {S}, C = {C}. Analyse ces résultats et fournis une synthèse structurée selon les consignes suivantes :
Identifie le style dominant (celui qui a le plus grand nombre de réponses).
Identifie un style secondaire uniquement si son nombre de réponses représente au moins 25 % du total des réponses.
Rédige la synthèse en français, de manière claire et directe, en respectant la structure suivante (utilise ces titres exacts en les mettant en gras) :
Résultats chiffrés : indique le nombre de réponses pour chaque style (D, I, S, C).
Style dominant : rédige une phrase claire identifiant le style principal.
Style secondaire : rédige une phrase précisant le style secondaire si le seuil de 25 % est atteint, ou indique qu’aucun style secondaire significatif n’est détecté.
Profil comportemental : rédige un texte de 200 à 300 mots qui décrit le profil de la personne en se basant exclusivement sur les styles identifiés (dominant et secondaire uniquement).
Conseils personnalisés : fournis 3 recommandations concrètes, spécifiquement adaptées aux traits du style dominant (et du style secondaire si présent).
Important : ne décris jamais de styles qui n’ont pas été détectés dans les résultats. La synthèse doit rester strictement cohérente avec les données fournies.'''
        with st.spinner("Analyse..."):
            result = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt_eval}]
            )
        st.markdown("## 📊 <strong>Résultat DISC</strong>", unsafe_allow_html=True)
        st.markdown(result.choices[0].message.content)