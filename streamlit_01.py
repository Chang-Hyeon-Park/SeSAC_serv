import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Basics")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
# 단순한 텍스트
st.text("This is a simple text")

# Write
# '변수' -> 문자열, 숫자, 리스트, 딕셔너리, 데이터프레임
st.write("This is a write dimension")
st.write(pd.DataFrame({'first' : [1,2,3,4],
                        'second' : [4,5,6,7]}))

# markdown
html_page = '''
<div style = "background-color:blue; padding:50px">
    <p style="color:yellow; font-size:5'px">Enjoy Stremlit!</p>
</div>
'''

# streamlit에서 html을 활용해서 페이지를 변경시킬 수 있음
st.markdown(html_page, unsafe_allow_html=True)