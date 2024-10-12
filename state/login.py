import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def login():
    st.session_state.state = 'login'

    st.title('Login')

    st.button('Login', on_click=change_state, args=['lost_or_found'])