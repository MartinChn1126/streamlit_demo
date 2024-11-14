import streamlit as st
import pandas as pd

st.header('销售单')

col1,col2,col4,col5 = st.columns([0.1,0.35,0.25,0.3],vertical_alignment='center')
col1.text('公司名:')
col2.text_input('Company name',label_visibility='collapsed')
col4.button('添加公司信息')
col5.markdown('订单号: :blue[{}]'.format(123456789))

col21,col22,col23,col24,col25 = st.columns([0.1,0.2,0.35,0.1,0.3],vertical_alignment='center')
col21.text('销售员:')
col22.text_input('销售员',label_visibility='collapsed')
col24.text("电话号码:")
col25.text_input('电话号码',max_chars=11,label_visibility='collapsed')


data = pd.DataFrame({'产品ID':[],'产品名称':[],'产品描述':[],'当前库存':[],'数量':[],'销售价格':[]})
st.data_editor(data,use_container_width=True,hide_index=True,num_rows='dynamic',column_config={'产品ID':st.column_config.NumberColumn(required=True),"销售价格":st.column_config.NumberColumn()})
