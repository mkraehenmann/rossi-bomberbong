import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def this_description_matches(authenticator):
    
    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))
    
    st.title('Does this description match?')
    st.write(st.session_state['hit_desc'])

    # if is your item go to someone_found page
    st.button('This description matches', on_click=change_state, args=['someone_lost'])

    # if is not your item go to profile page
    st.button('This description doesn\'t match', on_click=change_state, args=['profile'])