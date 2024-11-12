import streamlit as st
import pandas as pd
from init import AccountAuthority,upload_database


def get_authority():
    pass

def set_authority(usrname,*arg):
    pass


st.text('Change the authority of any user')
users_authority = st.session_state['db'].execute("SELECT USERNAME,AUTHORITY FROM USER")
data = pd.DataFrame(users_authority)
data.columns = ['username','authority']

st.data_editor(data,column_config={'authority':st.column_config.SelectboxColumn('Authority',options=list(AccountAuthority._member_names_),required=True)},hide_index=True,on_change=upload_database,key='accounts_authority',num_rows='dynamic')



st.button('Commit the change',on_click=upload_database)