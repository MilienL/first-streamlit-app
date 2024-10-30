import streamlit as st

st.title("Basic authentication password")

# Invite le user à créer un mdp
password = st.text_input("Veuillez créer un mot de passe :", type="password")

# Si le mot de passe est bien défini, on invite le user à le saisir
if password:
    st.success("Votre mot de passe a bien été créé.")

    user_password = st.text_input("Pour vous authentifier, veuillez saisir votre mot de passe :", type="password")

    if st.button("Vérifier le mot de passe"):
        if user_password == password:
            st.success("Bravo : mot de passe correct !", icon="✅")
        else:
            st.error("Mot de passe incorrect !", icon="🚨")