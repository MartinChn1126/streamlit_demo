import streamlit as st
import pandas as pd
from init import AccountAuthority,upload_database,query_database


def get_authority():
    pass

def set_authority(usrname,*arg):
    pass


def data_verification():

    changed = st.session_state['accounts_authority']
    if changed['edited_rows']:
        print('edited_rows: {}'.format(changed['edited_rows']))
    if changed['added_rows']:
        for item in changed['added_rows']:
            query_database('USER','')
            insert_stmt = 'INSERT USERNAME,PASSWORD,AUTHORITY INTO USER VALUES (?,?,?)'
            upload_database('USER',insert_stmt,(item['username'],'123456',item['password']))
    if changed['deleted_rows']:
        
        print('deleted_rows: {}'.format(changed['deleted_rows']))

def show_users_and_authorities():

    st.text("The following table lists all users and their authorities. You can change their authorities except 'Martin' as the Administrator unchangable.")
    users_authority = st.session_state['db'].execute("SELECT USERNAME,AUTHORITY FROM USER")
    data = pd.DataFrame(users_authority)
    data.columns = ['username','authority']

    st.data_editor(data,column_config={'authority':st.column_config.SelectboxColumn('Authority',options=list(AccountAuthority._member_names_),required=True)},hide_index=True,key='accounts_authority',num_rows='dynamic',on_change=data_verification)

    st.button('Commit the changes',on_click=upload_database)
    if 'accounts_authority' in st.session_state:
        st.write(st.session_state['accounts_authority'])


show_users_and_authorities()