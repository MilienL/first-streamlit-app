import streamlit as st
import requests

url = "https://swapi.dev/api/people/5/"
request = requests.get(url)
dic = request.json()

st.title("Display info from Star Wars API")

st.subheader(f"Appel API : {url}")

st.subheader("Affichage item JSON")

for item in dic.items():
    st.write(item)

st.subheader("Résumé")

if dic['gender'] == "male":
    st.write(f"{dic['name']} mesure {dic['height']} cm et pèse {dic['mass']} kg. Il est né en {dic['birth_year']}")
else:
    st.write(f"{dic['name']} mesure {dic['height']} cm et pèse {dic['mass']} kg. Elle est née en {dic['birth_year']}")