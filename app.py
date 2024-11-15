import streamlit as st
from init import *

init_web()

# add_examples_to_database(st.session_state['db'])

admins = get_all_adminstrators()

# reset_admin_password()

# query_database()

def generate_account_page():
    if (st.session_state['account'],) in admins:
        return [password_manage,accounts_manage]
    else:
        return [password_manage] # add some comments

if st.session_state['account']:
    
    pg = st.navigation({'Account':generate_account_page(),'Job':generate_pages()})
    with st.sidebar:
        with st.popover('{}'.format(st.session_state['account']),use_container_width=True):
            button = st.button('退出')
            change_pw = st.button('更改密码')
            if button:
                logout()
            if change_pw:
                st.switch_page(password_manage)
else:
    pg = st.navigation([signin_page,signup_page],position='hidden')
    

pg.run()
# st.switch_page(log_page)


