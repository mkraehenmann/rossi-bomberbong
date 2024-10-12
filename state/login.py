import streamlit as st
import yaml

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def login(authenticator, config):
    st.session_state.state = 'login'

    st.title('Login')    

    try:
        authenticator.login()
    except Exception as e:
        st.error(e)

    st.button('Register', on_click=change_state, args=['register'])

    if st.session_state['authentication_status']:
        authenticator.logout()
        st.write(f'Welcome *{st.session_state["name"]}*')
        change_state('lost_or_found')
        st.rerun()
        #st.button('Login', on_click=change_state, args=['lost_or_found'])    
    elif st.session_state['authentication_status'] is False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password')