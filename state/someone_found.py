import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def someone_found(authenticator):

    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    st.title('Someone Found Your Item')

    # go back to profile page
    st.button('Profile', on_click=change_state, args=['profile'])
