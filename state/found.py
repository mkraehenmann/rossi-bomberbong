import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def found():
    st.title('You Found Something ?')

    # go back to profile page
    st.button('Profile', on_click=change_state, args=['profile'])

    # if match go to someone_lost page
    st.button('found match', on_click=change_state, args=['someone_lost'])

    # if not match go to profile page
    st.button('not found match', on_click=change_state, args=['profile'])