import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def lost():
    st.title('Lost Page')

    st.button('Back', on_click=change_state, args=['lost_or_found'])