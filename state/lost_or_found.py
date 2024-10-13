import streamlit as st
# import streamlit_extras

from streamlit_extras.stylable_container import stylable_container


def change_state(state):
    if 'state' in st.session_state:
        st.session_state.state = state

def lost_or_found(authenticator):

    # go back to profile page
    st.sidebar.markdown(st.session_state.username)
    st.sidebar.button(
        label = 'Your Profile',
        on_click=change_state, 
        args=['profile'],
    )

    # logout
    authenticator.logout(location='sidebar', callback=lambda _: change_state("login"))

    # title
    st.title('Lost or Found')

    col1, col2 = st.columns(2)
    
    # Define buttons in the left and right columns
    with col1:
        with stylable_container(
            key="lost_button",
            css_styles="""
                button {
                    background-color: white;  /* Set background color to white */
                    color: black;  /* Use black text for contrast */
                    border-radius: 10px;
                    padding: 30px 60px;  /* Increase padding for a larger button */
                    font-size: 224px;  /* Set font size */
                    font-family: 'Inter', san-serif;
                    text-align: center;
                    display: inline-block;  /* Allows width adjustment */
                    width: 100%;  /* Full width of the column */
                    height: 500px;  /* Set fixed height for the button */
                    border: 3px solid lightgray;  /* Optional: add border to match the design */
                }
                """,
        ):
            st.button("Lost", on_click=change_state, args=["lost"])

    with col2:
        with stylable_container(
            key="found_button",
            css_styles="""
                button {
                    background-color: white;  /* Set background color to white */
                    color: black;  /* Use black text for contrast */
                    border-radius: 10px;
                    padding: 30px 60px;  /* Increase padding for a larger button */
                    font-size: 224px;  /* Set font size */
                    font-family: 'Inter', san-serif;
                    text-align: center;
                    display: inline-block;  /* Allows width adjustment */
                    width: 100%;  /* Full width of the column */
                    height: 500px;  /* Set fixed height for the button */
                    border: 3px solid lightgray;  /* Optional: add border to match the design */
                }
                button:hover {
                    background-color: gray;  /* Change background to gray on hover */
                    color: white;  /* Change text color to white on hover */
                }
                .label {
                    font-size: 54px;  /* Set font size for the label */
                    color: red;  /* Set label text color */
                    margin-bottom: 10px;  /* Space between label and content */
                }
                """,
        ):
            st.button("Found", on_click=change_state, args=["found"])
            #st.markdown('<div class="label">Custom Label</div>', unsafe_allow_html=True)