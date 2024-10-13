# set environment variable before:
    # for windows: $env:STREAMLIT_SERVER_ENABLE_STATIC_SERVING = 'true'
    # for linux: export STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true
# run with streamlit run app.py

import streamlit as st
# import folium

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from state.login import login
from state.register import register
from state.lost_or_found import lost_or_found
from state.lost import lost
from state.found import found
from state.profile import profile
from state.this_your_item import this_your_item
from state.this_description_matches import this_description_matches
from state.someone_found import someone_found
from state.someone_lost import someone_lost

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

# authenticate setup
with open('./config_auth.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# state machine
if 'state' not in st.session_state or st.session_state.state == 'login':
    login(authenticator, config)

elif st.session_state.state == 'register':
    register(authenticator, config)

elif st.session_state.state == 'lost_or_found':
    lost_or_found(authenticator)

elif st.session_state.state == 'lost':
    lost(authenticator)

elif st.session_state.state == 'found':
    found(authenticator)

elif st.session_state.state == 'profile':
    profile(authenticator)

elif st.session_state.state == 'this_your_item':
    this_your_item(authenticator)

elif st.session_state.state == 'this_description_matches':
    this_description_matches(authenticator)

elif st.session_state.state == 'someone_found':
    someone_found(authenticator)

elif st.session_state.state == 'someone_lost':
    someone_lost(authenticator)
