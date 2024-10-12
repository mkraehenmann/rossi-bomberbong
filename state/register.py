import streamlit as st
import yaml

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def register(authenticator, config):
    st.session_state.state = 'register'

    st.title('Register')

    try:
        email_of_registered_user, \
        username_of_registered_user, \
        name_of_registered_user = authenticator.register_user()
        if email_of_registered_user:
            st.success('User registered successfully')
            with open('./config_auth.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            change_state('login')
            st.rerun()
    except Exception as e:
        st.error(e)