import streamlit as st

from init import password_form_test,query_database

def test_origin(pw:str)->bool:
    if not pw:
        return True
    p = st.session_state['db'].execute("""SELECT PASSWORD FROM USER WHERE USERNAME=?""",(st.session_state['account'],)).fetchone()
    if p[0] == pw:
        return True
    else:
        return False

def confirm(*args):

    if not args[2]:
        return False
    for item in args:
        if not item:
            return False
    return True

def three_item(t1:str,t2:str,t3:str,test,t2_type:str|None='default'): # three items are text, text_input, text
    col1,col2,col3 = st.columns([0.08,0.3,0.6],vertical_alignment='center')
    col1.text(t1)
    text = col2.text_input(t2,type=t2_type,label_visibility='collapsed')
    if test(t2):
        col3.markdown(':red[{}]'.format(t3))
    else:
        return text
    
def change_password():


    origin_pw = three_item('旧密码:','输入旧密码','密码错误',test_origin)
    new_pw = three_item('新密码:','输入新密码','密码格式不允许',password_form_test,'password')
    confirm_pw = three_item('验证新密码:','验证密码输入','密码不相同',lambda x:False,'password')


    button = st.button('确认更改')

    if button:
        # update data in sql
        db = st.session_state['db']
        db.execute("""UPDATE USER SET PASSWORD =? WHERE USERNAME=?""",(new_pw,st.session_state['account']))
        db.commit()
        st.session_state['account'] = None
        st.rerun()

@st.dialog('确定重置密码')
def reset_pw():
    col1,col2,col3,col4 = st.columns([0.25,0.25,0.25,0.25])
    sure = col2.button('确定')
    cancel = col3.button('取消')
    if sure:
        db = st.session_state['db']
        db.execute('''UPDATE USER SET PASSWORD=? WHERE USERNAME=?''',(123456,st.session_state['account']))
        db.commit()
        st.session_state['account'] = None
        st.rerun()
    if cancel:
        st.rerun()

def reset_password():
    button = st.button('重置密码')
    if button:
        reset_pw()


tab2,tab1 = st.tabs(['密码重置','更改密码'])
with tab1:
    change_password()

with tab2:
    reset_password()



