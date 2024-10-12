import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def lost_or_found(authenticator):

    # go back to profile page
    st.sidebar.button(
        label = st.session_state.username, 
        on_click=change_state, 
        args=['profile'],
    )

    # logout
    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    # title
    st.title('Lost or Found')

    # go to the lost page
    st.button('Lost', on_click=change_state, args=['lost'])

    # go to the found page
    st.button('Found', on_click=change_state, args=['found'])