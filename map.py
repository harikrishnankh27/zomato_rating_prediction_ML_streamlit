import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def load_map():
    df2 = pd.read_csv('/home/user/project_web/map.csv')
    map_loc = df2[['Latitude', 'Longitude', 'count']]
    map_loc.loc[:, 'count'] = map_loc['count'].astype(float)

    # Remove rows with NaN values
    df2 = df2.dropna(subset=['Latitude', 'Longitude'])
    return df2

df2 = load_map()

def show_map_page():
    # Create a Folium Map object

     
    mapObj = folium.Map(location=[12.9716, 77.5946], zoom_start=12)

    scaling_factor = 0.1
    for i in range(len(df2)):
        lat = df2.iloc[i]['Latitude']
        lon = df2.iloc[i]['Longitude']
        rad = df2.iloc[i]['count']
        clr = 'red' if rad >= 1000 else 'blue'
        radius = (rad * scaling_factor) * 10
        folium.Circle(location=[lat, lon], color=clr, radius=radius, fill=True).add_to(mapObj)
    
    # Display the Folium Map
    st.write("<h1 style='font-size:36px;'>Clusters with most zomato online orders </h1>", unsafe_allow_html=True)

    st_folium(mapObj, width=800, height=600)  # Adjust width and height as per your requirements


