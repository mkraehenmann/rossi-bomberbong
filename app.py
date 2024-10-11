# run with streamlit run app.py

import streamlit as st
from state.login import login
from state.lost_or_found import lost_or_found
from state.lost import lost
from state.found import found


def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state


print(f'0: {st.session_state}')


if 'state' not in st.session_state or st.session_state.state == 'login':
    # st.session_state.state = 'login'
    # st.title('Login Page')
    # st.button('Login', on_click=change_state, args=['lost_or_found'])
    login()

elif st.session_state.state == 'lost_or_found':
    # st.title('Lost or Found Page')
    # st.button('Lost', on_click=change_state, args=['lost'])
    # st.button('Found', on_click=change_state, args=['found'])
    lost_or_found()


elif st.session_state.state == 'lost':
    # st.title('Lost Page')
    # st.button('Back', on_click=change_state, args=['lost_or_found'])
    lost()


elif st.session_state.state == 'found':
    # st.title('Found Page')
    # st.button('Back', on_click=change_state, args=['lost_or_found'])
    found()
