import streamlit as st
from db_manager import *
import pickle
import random
from sentence_transformers import SentenceTransformer, util
from PIL import Image
import json
import datetime
from datetime import datetime, timedelta
import random
import sys

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def find_match(img, description, time, location):
    
        # evaluate embedding
        img_model = SentenceTransformer('clip-ViT-B-32')
        img_emb = img_model.encode(img)

        # Insert found item into database
        id = random.getrandbits(32)
        item = Item(id, img, img_emb, description, time, location)
        db = Database()
        db.insert_item(item)
        u = db.get_user(st.session_state.username)
        db.insert_found_item(item, u)

        # TODO: Find match
        match_found = False

        db.close()

        if match_found:
            change_state('someone_lost')
        else:
            change_state('profile')

def found(authenticator):

    # go back to profile page
    st.sidebar.button(
        label = st.session_state.username, 
        on_click=change_state, 
        args=['profile'],
    )

    # logout
    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    # title
    st.title('Describe the item you found')

    # get image of found item
    st.subheader("What")
    img = None
    file = st.file_uploader("yea", type=["png", "jpg", "jpeg", "HEIC"], label_visibility='collapsed')
    if file is not None:
        img = Image.open(file)
        img = img.transpose(Image.ROTATE_270)
        st.image(img)
        
    # get location of found item
    with open('rooms.json', 'r') as file:
        locs = json.load(file)
    st.subheader('Where')
    location = st.selectbox(
        label = 'yea',
        options = locs,
        label_visibility='collapsed'
    )

    # get date it was found
    st.subheader("When")
    date = st.date_input(
        label="yea",
        value='today',
        max_value=datetime.now().date(),
        min_value=datetime.now().date() - timedelta(days=30),
        label_visibility='collapsed'
    )
    time = int(datetime.combine(date, datetime.min.time()).timestamp())
    
    st.button('Submit', on_click=find_match, args=[img, None, time, location])
    
    # # go back to profile page
    # st.button('Profile', on_click=change_state, args=['profile'])

    # # if match go to someone_lost page
    # st.button('found match', on_click=change_state, args=['someone_lost'])

    # # if not match go to profile page
    # st.button('not found match', on_click=change_state, args=['profile'])