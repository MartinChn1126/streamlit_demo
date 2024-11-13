import streamlit as st
from init import *

init_web()

# add_examples_to_database(st.session_state['db'])

admins = get_all_adminstrators()

def generate_account_page():
    if (st.session_state['account'],) in admins:
        return [accounts_manage]
    else:
        return [] # add some comments

if st.session_state['account']:
    
    pg = st.navigation({'Job':generate_func_pages('UIs'),'Account':generate_account_page()})
    with st.sidebar:
        button = st.button('{}'.format(st.session_state['account']))
        if button:
            logout()
else:
    pg = st.navigation([log_page,signup_page],position='hidden')
    

pg.run()
# st.switch_page(log_page)


