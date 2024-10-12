import streamlit as st

import folium
from streamlit_folium import st_folium
from datetime import datetime

import json

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def lost(authenticator):

    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    st.title("404NotLost")
    st.header('You Lost Something?')
    
    st.subheader("What?")
    st.write("Upload an image of the lost item")
    file = st.file_uploader("", type=["png", "jpg", "jpeg", "HEIC"])

    if file is not None:
        img = Image.open(file)
        img = img.transpose(Image.ROTATE_270)
        st.image(img)     
    
    """where"""

    st.subheader("Where?")
    st.write("Select the last known location of your item")
    # Initial location for the map

    # Create an empty session state variable for storing the latest clicked location
    if 'last_clicked_location' not in st.session_state:
        st.session_state.last_clicked_location = None
    
    if st.session_state.last_clicked_location != None:        
        st.session_state.location = st.session_state.last_clicked_location
        
    m = folium.Map(location=st.session_state.location, zoom_start=16)
    
    lat, lon = st.session_state.location
    # Add the marker at the clicked location
    folium.Marker([lat, lon], popup="Latest Location").add_to(m)

    # Add the ClickForMarker functionality to capture the new click location
    m.add_child(folium.ClickForMarker())
    
    # Render the Folium map in Streamlit
    st_data = st_folium(m, width=600, height=400)
    
    # If the user clicks on the map, update the session state with the new location
    if st_data and st_data['last_clicked'] is not None:
        st.session_state.last_clicked_location = (st_data['last_clicked']['lat'], st_data['last_clicked']['lng'])
        m.location = st.session_state.last_clicked_location
        st_data = st_folium(m, width=600, height=400)
    
    st.subheader("When?")
    
    current_datetime = datetime.now()

    # Create date selection
    selected_date = st.date_input("Select a date:", value=current_datetime.date())

    st.write(f"Date: {selected_date}")
        
    col1, col2 = st.columns(2)
    
    # if match go to this_your_item page
    with col1:
        st.button('found match', on_click=change_state, args=['this_your_item'])

    # if not match go to profile page
    with col2:
        st.button('not found match', on_click=change_state, args=['profile'])
        
    # go back to profile page
    st.button('Profile', on_click=change_state, args=['profile'])

    
    
    
    