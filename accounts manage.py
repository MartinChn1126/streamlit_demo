import streamlit as st
import pandas as pd
from init import AccountAuthority,update_database,query_database


def get_authority():
    pass

def set_authority(usrname,*arg):
    pass


def data_verification():

    changed = st.session_state['changed']
    origin_data = st.session_state['authorities']
    usernames = origin_data['username'].to_numpy()
    if edited_rows:=changed['edited_rows']:
        pass
    if add_rows := changed['added_rows']:
        add_items = []
        for item in add_rows:
            if item['username'] not in usernames:
                add_items.append((item['username'],'123456',item['authority']))
            else:
                st.text('{} has been created, you can only change its authority or first delete it then create new one'.format(item['username']))
        st.write(add_items)
        # change to use a more robust way.
        # st.session_state['db'].executemany("INSERT INTO USER VALUES",add_items)
    if deleted_rows:=changed['deleted_rows']:
        to_delete = origin_data['username'].iloc[deleted_rows].to_list()
        if 'Martin' in to_delete:
            to_delete.remove('Martin')
        else:
            pass
        st.write(to_delete)
        # st.session_state['db'].executemany("DELETE FROM USER WHERE USERNAME=?",to_delete)

def show_users_and_authorities():

    st.markdown("The following table lists all users and their authorities. You can change all user's authorities except ':blue[Martin]' who is the :blue[Administrator] unchangable.")

    users_authority = st.session_state['db'].execute("SELECT USERNAME,AUTHORITY FROM USER")
    data = pd.DataFrame(users_authority)
    data.columns = ['username','authority']
    st.session_state['authorities'] = data

    st.data_editor(data,column_config={'authority':st.column_config.SelectboxColumn('Authority',options=list(AccountAuthority._member_names_),required=True)},hide_index=True,key='changed',num_rows='dynamic',on_change=data_verification,use_container_width=True)

    st.button('Commit the changes',on_click=update_database)
    if 'changed' in st.session_state:
        st.write(st.session_state['changed'])


show_users_and_authorities()