import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from map import show_map_page
from table import show_table_page
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/967f19111202195.5ffdfc0e915cb.gif");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


page=st.sidebar.selectbox("PRDICT,EXPLORE,MAP,TABLE",("Predict","Explore","Map","Table"))

if page =="Predict":

    show_predict_page()
elif page=="Explore":
    show_explore_page()
elif page=="Table":

    show_table_page()
else:
    show_map_page()    