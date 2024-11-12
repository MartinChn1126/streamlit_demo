import streamlit as st
from app import log_page

def username_form_test(username) -> bool:
    pass

def password_form_test(password) -> bool:
    pass

    
def query_user(username):
    result = st.session_state['db'].execute("SELECT * FROM USER WHERE USERNAME = ?",(username,)).fetchone()
    if result:
        st.markdown(':red[{}] has been created!'.format(username))
        st.session_state['account'] = username


def signup_page():
    with st.container(border=True):
        col1,col2 = st.columns([0.5,0.5])
        first_name = col1.text_input('First Name')
        last_name = col2.text_input('Last Name')
        username = first_name + last_name
        password = st.text_input('Password',type='password')
        st.button('Sign up',on_click=query_user,args=(username,))
        st.text('Have an account?')
        st.page_link(log_page,label='login')

signup_page()