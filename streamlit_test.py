# run with streamlit run streamlit_test.py

import streamlit as st

# make a state machine page A -> page B

# page A
if 'page' not in st.session_state:
    st.session_state.page = 'A'

if st.session_state.page == 'A':
    st.write('Page A')
    if st.button('Go to page B'):
        st.session_state.page = 'B'

# page B
if st.session_state.page == 'B':
    st.write('Page B')
    if st.button('Go to page A'):
        st.session_state.page = 'A'