import streamlit as st
import requests

def get_character_info(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

st.title('Rick and Morty Character Information')

character_id = st.number_input('Enter character ID:', min_value=1, step=1)
if st.button('Get Character Info'):
    if character_id:
        character_data = get_character_info(character_id)
        if character_data:
            st.write(f"### Character Information for ID: {character_id}")
            st.write(f"Name: {character_data['name']}")
            st.image(character_data['image'], caption=f"{character_data['name']}'s Image")
            st.write(f"Status: {character_data['status']}")
            st.write(f"Species: {character_data['species']}")
            st.write(f"Gender: {character_data['gender']}")
            st.write(f"Origin: {character_data['origin']['name']}")
            st.write(f"Location: {character_data['location']['name']}")
        else:
            st.write("Character ID not found. Please enter a valid ID.")
    else:
        st.write("Please enter a character ID.")
