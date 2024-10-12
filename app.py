# run with streamlit run app.py

import streamlit as st

from state.login import login
from state.lost_or_found import lost_or_found
from state.lost import lost
from state.found import found
from state.profile import profile
from state.this_your_item import this_your_item
from state.someone_found import someone_found
from state.someone_lost import someone_lost



def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state


print(f'0: {st.session_state}')


if 'state' not in st.session_state or st.session_state.state == 'login':
    login()

elif st.session_state.state == 'lost_or_found':
    lost_or_found()

elif st.session_state.state == 'lost':
    lost()

elif st.session_state.state == 'found':
    found()

elif st.session_state.state == 'profile':
    profile()

elif st.session_state.state == 'this_your_item':
    this_your_item()

elif st.session_state.state == 'someone_found':
    someone_found()

elif st.session_state.state == 'someone_lost':
    someone_lost()
