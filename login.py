import streamlit as st
from enum import Enum


class UIFeedback(Enum):
    default = None
    username_empty = 'username empty'
    username_invalid = 'username invalid'
    username_exists = 'username exists'
    password_wrong = 'password wrong'


def feedback(username):

    match st.session_state['ui_feedback']:
        case UIFeedback.username_invalid:
            st.markdown(':blue[{}] is not a user.'.format(username))
        case UIFeedback.password_wrong:
            st.markdown(':red[Password invalid]')
        case UIFeedback.username_empty:
            st.text('Pls input a username')
        case _:
            pass

def query(username:str,password:str):
    result = st.session_state['db'].execute("SELECT USERNAME,PASSWORD FROM USER WHERE USERNAME = ?",(username,)).fetchone()
    if not result:
        st.session_state['ui_feedback'] = UIFeedback.username_invalid
    else:
        if (username,password) ==result:
            st.session_state['ui_feedback'] = UIFeedback.default
            st.session_state['logged_in'] = True
            st.toast('{} has logged in'.format(username))
        else:
            st.session_state['ui_feedback'] = UIFeedback.password_wrong


def username_cache():
    if 'account' not in st.session_state:
        return None
    else:
        return st.session_state['account']

def login_page():

    # create the login_in page
    with st.container(border=True):
        username = st.text_input('Name',value=username_cache(),placeholder='Martin')
        password = st.text_input('Password',type='password',placeholder='********')
        st.button('Sign in',on_click=login_test,args=(username,password))
        st.markdown("Don't have an account?[sign up](signup)")

def login_test(*args):
    # need to add code to query sql about the account logging information and create a variable `legally` to store the legally of logging, then return the variable `legally`
    username, password = args
    if not username:
        st.session_state['ui_feedback'] = UIFeedback.username_empty
    else:
        st.session_state['account'] = username
        query(username,password)
    feedback(username)

login_page()