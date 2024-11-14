import streamlit as st
import pandas as pd
from init import AccountAuthority,update_database,query_database
import re

def edit_rows():
    pass

def add_row():
    pass

def delete_rows():
    pass

def query_db():
    pass

def data_verification():
    db = st.session_state['db']

    changed = st.session_state['changed']
    origin_data = st.session_state['authorities']
    usernames = origin_data['username']
    if edited_rows:=changed['edited_rows']:
        need_to_update = []
        for index,authority in edited_rows.items():
            need_to_update.append((usernames.iloc[index],authority['authority']))
        st.write('Edited rows: {}.'.format(need_to_update))
    if add_rows := changed['added_rows']:
        add_items = []
        for item in add_rows:
            if item['username'] not in usernames.to_numpy():
                add_items.append({'username':item['username'],'authority':item['authority']})
            else:
                st.text('{} has been created, you can only change its authority or first delete it then create new one'.format(item['username']))
        st.write("Added rows: {}.".format(add_items))
        # change to transfer data to the server to do the real work.
        db.executemany("INSERT INTO USER (USERNAME,AUTHORITY) VALUES (:username,:authority)",add_items)
        db.commit()
    if deleted_rows:=changed['deleted_rows']:
        if 0 in deleted_rows:
            deleted_rows.remove(0)
            st.markdown(":red[Martin] is undeletable")
        to_delete = [(item,) for item in (origin_data['username'].iloc[deleted_rows].to_list())]
        st.write("Deleted username: {}.".format(to_delete))
        db.executemany("DELETE FROM USER WHERE USERNAME=?",to_delete)
        db.commit()

def show_users_and_authorities(): 
    # the main console of account manage ui

    st.markdown("The following table lists all users and their authorities. You can change all user's authorities except ':blue[Martin]'.")
                
    st.markdown("**Notice**: ':red[Martin]' is the :red[Administrator] which is unchangable or delible.")

    # change to use a global query function instead of use query function locallly.
    
    users_authority = st.session_state['db'].execute("SELECT USERNAME,AUTHORITY FROM USER")

    data = pd.DataFrame(users_authority)
    data.columns = ['username','authority']
    st.session_state['authorities'] = data

    st.data_editor(data,hide_index=True,key='changed',num_rows='dynamic',use_container_width=True,column_config={'authority':st.column_config.SelectboxColumn(options=list(AccountAuthority._member_names_[1:]),default='default'),'username':st.column_config.TextColumn(required=True,max_chars=10,validate="")})

    commit = st.button('Commit the changes')
    if commit:
        data_verification()
        # update_database()


show_users_and_authorities()