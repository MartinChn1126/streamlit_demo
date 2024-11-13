import streamlit as st
from init import UIFeedback,signup_page


def feedback(username):

    match st.session_state['ui_feedback']:
        case UIFeedback.username_invalid:
            st.markdown(':blue[{}] :red[is not a user].'.format(username))
        case UIFeedback.password_wrong:
            st.markdown(':red[Password invalid]')
        case UIFeedback.username_empty:
            st.markdown(':red[Pls input a username]')
        case _:
            pass

def query(username:str,password:str):
    result = st.session_state['db'].execute("SELECT USERNAME,PASSWORD FROM USER WHERE USERNAME = ?",(username,)).fetchone()
    if not result:
        st.session_state['ui_feedback'] = UIFeedback.username_invalid
    else:
        if (username,password) == result:
            st.session_state['ui_feedback'] = UIFeedback.default
            
            st.session_state['account'] = username
        else:
            st.session_state['ui_feedback'] = UIFeedback.password_wrong

def login_page():

    # create the login_in page
    with st.container(border=True):
        username = st.text_input('Name',placeholder='Martin')
        password = st.text_input('Password',type='password',placeholder='********')
        button = st.button('Sign in')
        with st.empty():
            feedback(username)
        col1,col2,col3,col4 = st.columns([0.25,0.25,0.25,0.25])
        col2.text("Don't have an account?")
        col3.page_link(signup_page)
        if button:
            if not username:
                st.session_state['ui_feedback'] = UIFeedback.username_empty
            else:
                query(username,password)
            st.rerun()

login_page()