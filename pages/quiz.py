import streamlit as st
import time

st.title("Quick Quiz")

st.subheader("3 questions - 3 erreurs possibles max")

# Définition d'une liste de dictionnaires contenant les questions, les propositions et les bonnes réponses
list_quest_answ = [
     {
        "question": "En quelle année est sortie l'album **Nevermind**, de **Nirvana** ?",
        "propositions": ["1979", "1987", "1991", "1995"],
        "correct_answer": 3
    },
    {
        "question": "Qui n'a jamais été membre des **Rolling Stones** ?",
        "propositions": ["Angus Young", "Keith Richards", "Charlie Watts", "Mick Jagger"],
        "correct_answer": 1
    },
    {
        "question": "Quel est l'album le plus vendu d'**AC/DC** ?",
        "propositions": ["Highway To Hell", "Back In Black", "Ballbreaker", "Black Ice"],
        "correct_answer": 2
    }
]

# Définition de variables d'état Streamlit
if "nb_remaining_errors" not in st.session_state:
    st.session_state.nb_remaining_errors = 3
    st.session_state.question_nb = 1

if st.session_state.question_nb < len(list_quest_answ)+1 and st.session_state.nb_remaining_errors > 0:
    # Affichage de la question
    current_question = list_quest_answ[st.session_state.question_nb - 1]
    st.write(f"Question {st.session_state.question_nb} : {current_question['question']}")

    # Affichage des options
    propositions = current_question["propositions"]
    user_answer = st.radio("Ta réponse:", propositions, index=None)

    # Bouton valider
    if st.button("Valider"):
        user_answer_index = propositions.index(user_answer) + 1

        if user_answer_index == current_question["correct_answer"]:
            st.success("Bonne réponse", icon="🎉")
            
            # Passer à la question suivante
            st.session_state.question_nb += 1
            time.sleep(1.5)
            st.rerun()
        else:
            st.error("Mauvaise réponse", icon="🤕")
            st.session_state.nb_remaining_errors -= 1

            if st.session_state.nb_remaining_errors == 1:
                st.warning("Il ne vous reste plus qu'une seule erreur possible", icon="🚨")
            elif st.session_state.nb_remaining_errors > 1:
                st.warning(f"Il ne vous reste plus que {st.session_state.nb_remaining_errors} erreurs possibles", icon="⚠️")

# Fin du quiz
#st.write(f"Remaining errors : {st.session_state.nb_remaining_errors}")
#st.write(f"Question nb : {st.session_state.question_nb}")
#st.write(f"Nb total questions : {len(list_quest_answ)}")

if st.session_state.nb_remaining_errors == 0:
    st.error("Vous avez perdu", icon="💀")
elif st.session_state.question_nb > len(list_quest_answ):
    st.success("Bravo champion.ne ! Tu as trouvé toutes les bonnes réponses")
    st.balloons()



