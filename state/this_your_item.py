import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def this_your_item():
    st.title('Is This Your Item ?')

    # if is your item go to someone_found page
    st.button('This is my item', on_click=change_state, args=['someone_found'])

    # if is not your item go to profile page
    st.button('This is not my item', on_click=change_state, args=['profile'])