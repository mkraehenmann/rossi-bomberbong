import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def someone_lost():
    st.title('Someone Lost the Item you Found') 

    # go back to profile page
    st.button('Profile', on_click=change_state, args=['profile'])