import streamlit as st

st.title("Interests calculation")

amount_placed = st.number_input("Combien d'argent (en euros) souhaites-tu investir ?", min_value=0.0, step=5.0, format="%.2f")
years = st.number_input("Pour combien d'années souhaites-tu investir ?", min_value=1, step=1, format="%d")
interest_rate = st.number_input("Quel est le taux d'intérêt ? (nombre décimal, ex : 0.05 pour 5%)", min_value=0.0, step=0.01, format="%.4f")

if st.button("Calculer"):
    final_amount = amount_placed
     
    for i in range(0, years):
       final_amount = final_amount * (1 + interest_rate)

    st.write(f"Pour un placement de {amount_placed} € sur {years} années avec un taux de {interest_rate} par an :")
    st.write(f"Ton patrimoine final sera de **{round(final_amount, 2)} €**")
    
