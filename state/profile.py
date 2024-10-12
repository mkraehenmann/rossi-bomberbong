import streamlit as st

def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def profile():
    st.title('Profile')

    # go back to the lost or found page
    st.button('Lost or Found something?', on_click=change_state, args=['lost_or_found'])

    # go to this_your_item page if somone found your item
    st.button('someone found your item', on_click=change_state, args=['this_your_item'])

    # go to someone_lost page if somone lost the item you found
    st.button('someone lost the item you found', on_click=change_state, args=['someone_lost'])
