import streamlit as st
import pandas as pd



def load_table():
    df = pd.read_csv('/home/user/project_web/zomato_project.csv')
    

    
    return df

df= load_table()

def show_table_page():
    st.title("Explore EDA evaluation")
    st.write("<h1 style='font-size:36px;'>Zomato serviced Hotel data in  Bangalore</h1>", unsafe_allow_html=True)

    st.write("DataFrame:")
    st.dataframe(df)  
    st.write("<h1 style='font-size:36px;'>Missing Values</h1>", unsafe_allow_html=True)

    ms=df.isna().sum()
    st.dataframe(ms)

    
    
        
    
st.set_option('deprecation.showPyplotGlobalUse', False)

