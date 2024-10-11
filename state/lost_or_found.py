import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def lost_or_found():
    st.title('Lost or Found Page')

    st.button('Lost', on_click=change_state, args=['lost'])
    st.button('Found', on_click=change_state, args=['found'])