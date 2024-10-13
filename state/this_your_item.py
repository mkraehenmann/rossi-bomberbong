import streamlit as st
from db_manager import *

def change_state(state):
    # add match to db
    if 'someone_found' in state:
        db = Database()
        st.session_state['hit_id']
        db.insert_match(st.session_state['hit_id'], st.session_state['it_id'])
    if 'state' in st.session_state:
        st.session_state.state = state

def this_your_item(authenticator):
    
    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))
    
    st.title('Is This Your Item ?')
    st.image(st.session_state['hit_img'])

    # if is your item go to someone_found page
    st.button('This is my item', on_click=change_state, args=['someone_found'])

    # if is not your item go to profile page
    st.button('This is not my item', on_click=change_state, args=['profile'])