import streamlit as st
from enum import Enum
import sqlite3
from os import listdir,sep

class AccountAuthority(Enum):
    administrator = 'admin'
    saler = 'saler'
    worker = 'worker'
    stockman = 'stockman'
    default = 'default'

class UIFeedback(Enum):
    default = None
    username_empty = 'username empty'
    username_invalid = 'username invalid'
    username_exists = 'username exists'
    password_wrong = 'password wrong'


def hide_menu_set():
    st.set_page_config('Main Page',layout='wide')
    st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stAppHeader{display:none}
    </style>
""", unsafe_allow_html=True)

    """st.html('''<style>
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        .stAppToolbar {display:none}
        ._terminalButton_rix23_138 {display:none}

</style>''')"""
    
hide_menu_set()

def database_init():

    user_db = sqlite3.connect('./db/all.db',check_same_thread=False)

    create_user_table = '''CREATE TABLE IF NOT EXISTS USER(
    USERNAME TEXT PRIMARY KEY NOT NULL,
    PASSWORD TEXT DEFAULT "123456",
    AUTHORITY TEXT DEFAULT "default");
    CREATE UNIQUE INDEX IF NOT EXISTS USERID ON USER(USERNAME)
    '''
    user_db.executescript(create_user_table)

    st.session_state['db'] = user_db

def init_web():

    if 'ui_feedback' not in st.session_state:
        st.session_state['ui_feedback'] = UIFeedback.default

    if 'account' not in st.session_state:
        st.session_state['account'] = None

    if 'querying'not in st.session_state:
        st.session_state['querying'] = []

    if 'uploading' not in st.session_state:
        st.session_state['uploading'] = []

    database_init()

def add_examples_to_database(db:sqlite3.Connection):
    l = [('Martin','123','administrator'),('Lilly','4546','saler'),('Nancy','123456','worker'),('Andrew','123456','stockman')]
    # Todo change the 'admin' above line to custom AccountAuthority and save in database
    insert_user = "INSERT INTO USER VALUES (?,?,?)"
    db.executemany(insert_user,l)
    db.commit()

@st.dialog('Logout?')
def logout():
    col1,col2,col3,col4 = st.columns([0.25,0.25,0.25,0.25])
    confirm = col2.button('Logout')
    cancel = col3.button('Cancel')

    if confirm:
        st.session_state['account'] = None
        st.rerun()
    elif cancel:
        st.rerun()

def delete_data_from_database(table:str,stmts:str):
    pass

def query_database():
    db = st.session_state['db']
    data = db.execute("SELECT * FROM USER")
    st.write(data)

def update_database(table:str,stmts:str,*args):
    """
    upload data to the current database with specified table and columns.
    Parameters:
    ----------
    table: the table name in the database to upload data to,

    """

    if 'data' not in st.session_state or not st.session_state['data']:
        pass
    else:
        db = st.session_state['db']

def add_data_to_database(table:str,stmts:str,*args):
    pass

def generate_pages(path:str='uis')->dict: # path is the directory where pages are saved. In this case, it is 'uis'
    pages = []
    for item in listdir('./'+path):
        pages.append(st.Page('.'+sep+path+sep+item))
    return pages

def get_all_adminstrators():
    admins = st.session_state['db'].execute("""SELECT USERNAME FROM USER WHERE AUTHORITY=?""",('administrator',))
    return admins

signin_page = st.Page('sign in.py',url_path='sign in')
signup_page = st.Page('sign up.py',url_path='signup')

accounts_manage = st.Page('accounts manage.py',url_path='account')

