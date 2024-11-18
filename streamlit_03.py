import streamlit as st

# HTML
html_page = """
<div style = "background-color:blue; padding:50px">
    <p style="color:yellow; font-size:5'px">Enjoy Stremlit!</p>
</div>
"""

st.markdown(html_page, unsafe_allow_html=True)

st.success("Success!")

st.info("Information")
st.warning("This is a warning")
st.error("This is an error!")
