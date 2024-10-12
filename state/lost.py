import streamlit as st

import folium
from streamlit_folium import st_folium
from datetime import datetime

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def lost(authenticator):

    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    st.title("404NotLost")
    st.header('You Lost Something?')
    
    st.subheader("What?")   
        
    st.subheader("Where?")
    st.write("Select the last known location of your item")
    
    # center on Liberty Bell, add marker  47.376234009886616, 8.547658923119648
    m = folium.Map(location=[47.376234, 8.5476589], zoom_start=16)
    folium.Marker(
        [47.376234, 8.5476589], popup="<i>ETHZ<i>", tooltip="RossiBomberBong"
    ).add_to(m)
    
    m.add_child(folium.ClickForLatLng())
    
    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=600, height=300)
    
    # If the user clicked on the map, st_data will have click information
    if st_data and 'last_clicked' in st_data:
        clicked_location = st_data['last_clicked']
        st.write(f"You clicked at: {clicked_location}")
        
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

    
    
    
    