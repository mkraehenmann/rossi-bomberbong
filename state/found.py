import streamlit as st
from db_manager import *
import pickle
# from sentence_transformers import SentenceTransformer, util
from PIL import Image

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def found(authenticator):

    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    st.title('You Found Something ?')
    st.write("Upload an image of the found item")
    file = st.file_uploader("", type=["png", "jpg", "jpeg", "HEIC"])

    """
    if file is not None:
        img = Image.open(file)
        img = img.transpose(Image.ROTATE_270)
        st.image(img)  

        # evaluate embedding
        img_model = SentenceTransformer('clip-ViT-B-32')
        img_emb = img_model.encode(img)
        
        # add to db
        db = Database()
        i = Item(1, img, img_emb, "", 0, "")
        db.insert_item(i)
        db.insert_found_item(i, st.session_state.user)
    """

    # go back to profile page
    st.button('Profile', on_click=change_state, args=['profile'])

    # if match go to someone_lost page
    st.button('found match', on_click=change_state, args=['someone_lost'])

    # if not match go to profile page
    st.button('not found match', on_click=change_state, args=['profile'])