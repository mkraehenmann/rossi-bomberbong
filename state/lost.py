import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def lost():
    st.title('You Lost Something ?')

    # go back to profile page
    st.button('Profile', on_click=change_state, args=['profile'])

    # if match go to this_your_item page
    st.button('found match', on_click=change_state, args=['this_your_item'])

    # if not match go to profile page
    st.button('not found match', on_click=change_state, args=['profile'])