import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

import folium
from streamlit_folium import st_folium

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def lost():
    st.title('You Lost Something ?')

    file = st.file_uploader("Upload an image of the lost item", type=["png", "jpg", "jpeg", "HEIC"])

    if file is not None:
        img = Image.open(file)
        img = img.transpose(Image.ROTATE_270)
        st.image(img)     

    # go back to profile page
    st.button('Profile', on_click=change_state, args=['profile'])

    # if match go to this_your_item page
    st.button('found match', on_click=change_state, args=['this_your_item'])

    # if not match go to profile page
    st.button('not found match', on_click=change_state, args=['profile'])
    
    # center on Liberty Bell, add marker  47.376234009886616, 8.547658923119648
    m = folium.Map(location=[47.376234, 8.5476589], zoom_start=16)
    folium.Marker(
        [47.376234, 8.5476589], popup="<i>ETHZ<i>", tooltip="RossiBomberBong"
    ).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=600)
    
    
    