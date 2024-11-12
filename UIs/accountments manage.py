import streamlit as st
import pandas as pd
from enum import Enum

class AccountAuthority(Enum):
    administrators = 'admin'
    salers = 'saler'
    workers = 'workers'
    stockmans = 'stockmans'
    default = 'basic'

def get_authority():
    pass

def set_authority(usrname,*arg):
    pass

def update_account_authority():
    st.write(st.session_state['accounts_authority']['added_rows'])

users_authority = st.session_state['db'].execute("SELECT USERNAME,AUTHORITY FROM USER")
data = pd.DataFrame(users_authority)
data.columns = ['username','authority']

st.data_editor(data,column_config={'authority':st.column_config.SelectboxColumn('Authority',options=list(AccountAuthority._member_names_),required=True)},hide_index=True,on_change=update_account_authority,key='accounts_authority',num_rows='dynamic')

