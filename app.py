
import streamlit as st
import openai
import random
import re
from collections import Counter

# Initialisation client OpenAI
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Fonction pour estimer le coût
def estimer_cout(model, tokens_in, tokens_out):
    prix = {
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        "gpt-4-turbo": {"input": 0.01, "output": 0.03}
    }
    p = prix[model]
    cout = (tokens_in / 1000) * p["input"] + (tokens_out / 1000) * p["output"]
    return round(cout, 4)

st.set_page_config(page_title="Test DISC", layout="centered")
st.title("🧠 Test DISC – Analyse de profil comportemental")

context = st.selectbox("Contexte", ["Professionnel", "Personnel", "Équipe"])
langue = st.selectbox("Langue", ["Français", "Anglais"])
niveau = st.selectbox("Niveau de langage", ["Grand public", "Étudiant", "Manager"])
nb_questions = st.slider("Nombre de questions", 10, 28, 12)
model = st.selectbox("Modèle GPT utilisé", ["gpt-3.5-turbo", "gpt-4-turbo"])

# Estimation coût
tokens_input = 1500
tokens_output = 4000
estimation = estimer_cout(model, tokens_input, tokens_output)
st.info(f"💰 Estimation du coût API : **~${estimation}** pour ce test complet ({model})")

if st.button("Générer le questionnaire"):
    prompt_gen = f"""
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
"""
    with st.spinner("Génération en cours..."):
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt_gen}]
        )
    questions_raw = response.choices[0].message.content.strip().split("\n\n")
    st.session_state["questions"] = questions_raw
    st.session_state["options_melangees"] = {}  # reset ordre mélangé

if "questions" in st.session_state:
    st.subheader("📝 Répondez au questionnaire")
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

        st.markdown(f"### ❓ Q{i+1}. {question_text.strip()}")
        selection = st.radio(
            label=" ",
            options=option_labels,
            index=None,
            key=f"q{i}",
            label_visibility="collapsed"
        )
        st.markdown("---")

        for opt in options_cleaned:
            if opt["text"] == selection:
                responses.append(opt["style"])
                break

    if st.button("Analyser mes réponses"):
        counts = Counter(responses)
        prompt_eval = f"""
Tu es un expert DISC. Voici les réponses codées d'un utilisateur à un questionnaire DISC : {dict(counts)}

1. Indique le nombre de réponses pour chaque style DISC (D, I, S, C).
2. Déduis la couleur dominante.
3. Donne la couleur secondaire si elle existe.
4. Rédige un profil synthétique (200-300 mots).
5. Fournis 3 conseils personnalisés selon ce profil.
"""
        with st.spinner("Analyse..."):
            result = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt_eval}]
            )
        st.subheader("📊 Résultat DISC")
        st.markdown(result.choices[0].message.content)
