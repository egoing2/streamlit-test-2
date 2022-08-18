import streamlit as st
view = [100, 200, 150]
st.write('# 유튜브 조회수')
st.write('## raw data')
view
st.write('## line chart')
st.line_chart(view)