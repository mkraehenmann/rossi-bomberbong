import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime
from db_manager import *
from sentence_transformers import SentenceTransformer, util
import torch


import json

def create_map(predefined_locations):
    # Initialize the map
    initial_location = [47.376234, 8.547658]  # Centered on ETHZ
    m = folium.Map(location=initial_location, zoom_start=16)

    # Add predefined markers
    for name, coords in predefined_locations.items():
        folium.Marker(location=coords, popup=name, tooltip=name).add_to(m)

    # Add ClickForLatLng to the map
    m.add_child(folium.ClickForLatLng())

    return m

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def lost(authenticator):

    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    st.title("404NotLost")
    st.header('You Lost Something?')
    
    st.subheader("What?")
    desc = st.text_input("Description of the object: ")
    model = SentenceTransformer('clip-ViT-B-32-multilingual-v1')
    desc_emb = model.encode([desc])
    # retrieve all items embedding
    db = Database()
    items = db.get_items()
    imgs_emb = [torch.from_numpy(item.emb) for item in items]
 
    # get top 10 items
    hits = util.semantic_search(torch.from_numpy(desc_emb), imgs_emb, top_k=10)[0]
    print("Query:")
    for hit in hits:
        print(hit['score'])

        st.image(items[hit['corpus_id']].image)


    st.write("Upload an image of the lost item")
    file = st.file_uploader("", type=["png", "jpg", "jpeg", "HEIC"])

    if file is not None:
        img = Image.open(file)
        img = img.transpose(Image.ROTATE_270)
        st.image(img)     
    
    """where"""

    st.subheader("Where?")
    st.write("Select the last known location of your item")
    
    # Carica i dati dal file JSON
    with open('rooms.json', 'r') as file:
        luoghi = json.load(file)
        
    print(luoghi)
    # Checkbox per 'unknown'
    unknown = st.checkbox("Non conosco il luogo")

    if unknown:
        st.write("Hai selezionato 'Unknown'.")
        # Non mostrare le dropdowns se si seleziona 'unknown'
        luogo_selezionato = "Unknown"
        edificio_selezionato = "Unknown"
        stanza_selezionata = "Unknown"
    else:
        # Selezione del luogo
        luogo_selezionato = st.selectbox("Seleziona un Luogo:", ["Unknown"] + list(luoghi.loc()))
        
        if luogo_selezionato != "Unknown":
            # Selezione dell'edificio
            edifici = luoghi[luogo_selezionato]
            edificio_selezionato = st.selectbox("Seleziona un Edificio:", ["Unknown"] + list(edifici.room()))
            
            if edificio_selezionato != "Unknown":
                # Selezione della stanza
                stanze = edifici[edificio_selezionato]
                stanza_selezionata = st.selectbox("Seleziona una Stanza:", ["Unknown"])
            else:
                stanza_selezionata = "Unknown"
        else:
            edificio_selezionato = "Unknown"
            stanza_selezionata = "Unknown"

    # Mostra le selezioni
    st.write(f"Luogo Selezionato: {luogo_selezionato}")
    st.write(f"Edificio Selezionato: {edificio_selezionato}")
    st.write(f"Stanza Selezionata: {stanza_selezionata}")
    """
    # Initial location for the map
    initial_location = [47.376234009886616, 8.547658923119648]

    # Create a Folium map centered on the initial location
    m = folium.Map(location=initial_location, zoom_start=16)

    # Add a ClickForLatLng feature to the map
    m.add_child(folium.ClickForLatLng())

    # Render the Folium map in Streamlit
    st_data = st_folium(m, width=600, height=300)

    # Check if the user clicked on the map
    if st_data and 'last_clicked' in st_data:
        clicked_location = st_data['last_clicked']

        # Make sure clicked_location is not None
        if clicked_location is not None:
            # Extract latitude and longitude
            lat, lon = tuple(clicked_location.values())

            # Create and add the new marker at the clicked location
            folium.Marker(
                location=[lat, lon],
                popup="<i>Selected Location</i>",
                tooltip="Current Location"
            ).add_to(m)

            # Re-render the updated map with the new marker
            st_data = st_folium(m, width=600, height=300)

            # Display the clicked location
            st.write(f"You clicked at: Latitude: {lat}, Longitude: {lon}")"""
            
            
    st.subheader("When?")
    
    st.write("Select the time when you lost your item")
    current_time = datetime.now().time()
    # Add a time input widget with the default time set to now
    selected_time = st.time_input("Select a time:", value=current_time)

    # Display the selected time
    st.write(f"Selected time: {selected_time}")
        
    col1, col2 = st.columns(2)
    
    # if match go to this_your_item page
    with col1:
        st.button('found match', on_click=change_state, args=['this_your_item'])

    # if not match go to profile page
    with col2:
        st.button('not found match', on_click=change_state, args=['profile'])
        
    # go back to profile page
    st.button('Profile', on_click=change_state, args=['profile'])

    
    
    
    