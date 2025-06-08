import streamlit as st
import openai
import random

# Initialisation API
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Test DISC", layout="centered")
st.title("Test DISC – Analyse de profil comportemental")

context = st.selectbox("Contexte", ["Professionnel", "Personnel", "Équipe"])
langue = st.selectbox("Langue", ["Français", "Anglais"])
niveau = st.selectbox("Niveau de langage", ["Grand public", "Étudiant", "Manager"])
nb_questions = st.slider("Nombre de questions", 10, 28, 12)

if st.button("Générer le questionnaire"):
    prompt_gen = f"""
Tu es un expert DISC. Crée {nb_questions} questions DISC adaptées au contexte {context.lower()}, en {langue.lower()}, pour un niveau de langage {niveau.lower()}.

Chaque question doit proposer 4 affirmations, correspondant chacune à un des 4 profils DISC (Dominance, Influence, Stabilité, Conformité), dans un ordre aléatoire. Évite tout biais de formulation.

Format :
Q1. Texte de la question
- A. Réponse
- B. Réponse
- C. Réponse
- D. Réponse
"""
    with st.spinner("Génération en cours..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt_gen}]
        )
    questions_raw = response.choices[0].message.content
    st.session_state["questions"] = questions_raw.split("\n\n")

if "questions" in st.session_state:
    st.subheader("Répondez au questionnaire")
    responses = []
    for i, bloc in enumerate(st.session_state["questions"]):
        lines = bloc.strip().split("\n")
        if len(lines) < 5:
            continue
        question = lines[0]
        options = lines[1:5]
        random.shuffle(options)
        answer = st.radio(question, options, key=f"q{i}")
        responses.append(answer[0])

    if st.button("Analyser mes réponses"):
        joined = ", ".join(responses)
        prompt_eval = f"""
Tu es un expert DISC. Analyse ces réponses : [{joined}]
- A = Dominance
- B = Influence
- C = Stabilité
- D = Conformité

Donne :
- Nombre de réponses par style
- Couleur dominante
- Couleur secondaire
- Profil synthétique (200-300 mots)
- 3 conseils personnalisés
"""
        with st.spinner("Analyse..."):
            result = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt_eval}]
            )
        st.subheader("Résultat DISC")
        st.markdown(result.choices[0].message.content)
