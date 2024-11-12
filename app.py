import streamlit as st
from enum import Enum
import sqlite3

def hide_menu_set():
    st.set_page_config('Page Title',layout='wide')
    st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        
        ._terminalButton_rix23_138" {display:none}
    </style>
""", unsafe_allow_html=True)

    st.html('''<style>
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        .stAppToolbar {display:none}
        ._terminalButton_rix23_138 {display:none}

</style>''')
    
hide_menu_set()


class AccountAuthority(Enum):
    administrators = 'admin'
    salers = 'saler'
    workers = 'workers'
    stockmans = 'stockmans'
    default = 'basic'


def database_init():

    user_db = sqlite3.connect('./db/user.db',check_same_thread=False)

    create_user_table = '''CREATE TABLE IF NOT EXISTS USER(
    USERNAME TEXT PRIMARY KEY,
    PASSWORD TEXT,
    AUTHORITY TEXT);
    CREATE UNIQUE INDEX IF NOT EXISTS USERID ON USER(USERNAME)
    '''
    user_db.executescript(create_user_table)

    if 'db' not in st.session_state:
        st.session_state['db'] = user_db

def add_example_to_database(db:sqlite3.Connection):
    l = [('Martin','123','administrators'),('Lilly','4546','salers')]
    # Todo change the 'admin' above line to custom AccountAuthority and save in database
    insert_user = "INSERT INTO USER VALUES (?,?,?)"
    for usern,pw,authority in l:
        db.execute(insert_user,(usern,pw,authority))
    db.commit()



def disconnect(db:sqlite3.Connection):
    db.close()


def page_configuration():
    st.set_page_config(page_title=None,layout='wide')
    st.markdown("""
        <style>
            .reportview-container {
                margin-top: -2em;
            }
            #MainMenu {visibility: hidden;}
            .stDeployButton {visibility:hidden,disply:None}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
        </style>""", unsafe_allow_html=True
)

# page_configuration()

def init_web():
    if 'ui_feedback' not in st.session_state:
        st.session_state['ui_feedback'] = None

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        # st.session_state['account'] = 'admin'
    database_init()

init_web()
# add_example_to_database(st.session_state['db'])

def generate_pages(page):
    if st.session_state['account'] == 'Martin':
        return [page]
    else:
        return []
    
work = st.Page('UIs/work.py')
sample_image = st.Page('UIs/image sample.py')
accounts_manage = st.Page('UIs/accountments manage.py',url_path='account')
history = st.Page('UIs/history.py')
report = st.Page('UIs/reports.py')


if st.session_state['logged_in']:
    pg = st.navigation({'Account':generate_pages(accounts_manage),'Job':[work,sample_image,history,report]})
    
else:
    log_page = st.Page('login.py',url_path='login')
    sign_up = st.Page('sign up.py',url_path='signup')
    pg = st.navigation([log_page,sign_up],position='hidden')

pg.run()
# st.switch_page(log_page)


