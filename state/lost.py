import random
import streamlit as st
from PIL import Image
# import folium
# from streamlit_folium import st_folium
from datetime import datetime, timedelta
import folium
from streamlit_folium import st_folium
from datetime import datetime
from db_manager import *
from sentence_transformers import SentenceTransformer, util
import torch


import json
from db_manager import *

# def create_map(predefined_locations):
#     # Initialize the map
#     initial_location = [47.376234, 8.547658]  # Centered on ETHZ
#     m = folium.Map(location=initial_location, zoom_start=16)

#     # Add predefined markers
#     for name, coords in predefined_locations.items():
#         folium.Marker(location=coords, popup=name, tooltip=name).add_to(m)

#     # Add ClickForLatLng to the map
#     m.add_child(folium.ClickForLatLng())

#     return m


def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def find_match(img, description, time, location):

    # Insert lost item into database
    id = random.getrandbits(32)
    item = Item(id, None, None, description, time, location)
    db = Database()
    db.insert_item(item)
    u = db.get_user(st.session_state.username)
    db.insert_lost_item(item, u)

    # TODO: Find match
    match_found = False

    db.close()

    if match_found:
        change_state('this_your_item')
    else:
        change_state('profile')

def lost(authenticator):

    # go back to profile page
    st.sidebar.button(
        label = st.session_state.username, 
        on_click=change_state, 
        args=['profile'],
    )

    # logout
    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    # title
    st.title("Describe the item you lost")
    st.write('Required items are marked with an asterisk.')
    
    # get description of lost item
    st.subheader("What *")
    description = st.text_area(
        label="yea",
        value="Provide a description",
        label_visibility='collapsed'
    )

    # get last known location of lost item
    with open('rooms.json', 'r') as file:
        locs = json.load(file)
    st.subheader('Where')
    location = st.selectbox(
        label = 'yea',
        options = locs,
        label_visibility='collapsed'
    )

    # get date it was lost
    st.subheader("When")
    date = st.date_input(
        label="yea",
        value='today',
        max_value=datetime.now().date(),
        min_value=datetime.now().date() - timedelta(days=30),
        label_visibility='collapsed'
    )
    time = int(datetime.combine(date, datetime.min.time()).timestamp())

    # get image of lost item
    """img = None
    st.subheader("Image")
    file = st.file_uploader(
        label="yea", 
        type=["png", "jpg", "jpeg", "HEIC"],
        label_visibility='collapsed'
    )
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
        st.image(img)  """
    
    # get time it was lost
    """
    current_time = datetime.now().time()
    time = st.time_input(
        label="yea",
        value='now',
        label_visibility='collapsed'
    )
    """
    
    # map
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
            
    # Find match
    st.button('Find Match', on_click=find_match, args=[None, description, time, location])
    
    
    
    