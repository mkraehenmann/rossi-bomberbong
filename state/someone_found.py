import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from db_manager import *


def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def someone_found(authenticator):
    db = Database()

     # go back to profile page
    st.sidebar.markdown(st.session_state.username)
    st.sidebar.button(
        label = 'Your Profile',
        on_click=change_state, 
        args=['profile'],
    )
    
    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    st.title('Someone Found Your Item')
        
    # First column with label for the image
    with stylable_container(
        key="image_container",
        css_styles=""""""
            ):
        st.image(db.get_item(st.session_state['hit_id']).image)
        st.write(db.get_item(st.session_state['it_id']).description)

    # Second column with label for buttons
    st.write("")
    with stylable_container(key="yes_button",
        css_styles="""
            button {
                background-color: #34A853;  /* Set background color to white */
                color: white;  /* Use black text for contrast */
                border-radius: 10px;
                padding: 30px 60px;  /* Increase padding for a larger button */
                font-size: 224px;  /* Set font size */
                font-family: 'Inter', san-serif;
                text-align: center;
                display: inline-block;  /* Allows width adjustment */
                width: 100%;  /* Full width of the column */
                height: 80px;  /* Set fixed height for the button */
                border: 3px solid lightgray;  /* Optional: add border to match the design */
            }"""):
        st.subheader("Your contact:")
        st.write(db.get_users()[1].username)
        st.write(db.get_users()[1].email)

    # go back to profile page
    st.button('Profile', on_click=change_state, args=['profile'])
